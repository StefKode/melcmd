#
# This file is part of the melcmd distribution (https://github.com/StefKode/melcmd).
# Copyright (c) 2021 Stefan Koch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################################
from api.mel_api_base import MelAPIBase
from factory.base import MelCmdFactory
import web.web_exceptions as WebErr
from api import mel_api_exceptions as ApiErr
from api.html_headers import Headers
from device.mel_device import MelDevice
import json


class MelAPI(MelAPIBase):
    """Provides access to functions of the MelCloud"""
    _context_key = None
    _cached_building = None

    def __init__(self, fac:MelCmdFactory, username:str, password:str):
        """
        Constructor of API object. The login credentials cannot be updated after creation.
        :param username: username string
        :param password: password string
        """
        self._make = fac
        self._web = self._make.WebTransport()
        self._username = username
        self._password = password
        self._headers = Headers()
        self._urls = self._make.Urls()
        self._log = self._make.Log("MelAPI")

    def _login(self) -> bool:
        """
        Login to MelCloud using username and password properties
        The login session is represented by the context_key property.
        Login() can be called any time again.
        This function does not throw any expected exception, instead it returns False
        if such an exception is
        :return: True if login was successful, False if otherwise.
        """
        login = '{"Email":"%s"' % self._username
        login += ',"Password":"%s"' % self._password
        login += ',"Language":4,"AppVersion":"1.22.8.0",'
        login += '"Persist":false,"CaptchaResponse":null}'
        self._log.print("start login")
        self._headers.delete('x-mitscontextkey')
        self._headers.set('content-type', "application/json; charset=UTF-8")
        try:
            response = self._web.post_jsn(url=self._urls.login,
                                    headers=self._headers.all,
                                    data=login)
        except Exception as e:
            print(e)
            self._context_key = None
            return False

        self._context_key = response['LoginData']['ContextKey']
        self._log.print("ContextKey = " + str(self._context_key))
        self._headers.set('x-mitscontextkey', self._context_key)
        self._headers.delete('content-type')
        return True

    def _web_cmd_post(self, url:str, data:dict):
        """
        Post a dictionary (data) to the specified url
        This method is a convenience function, it calls the universal _web_cmd with
        the desired Web transport method (static)
        :return: dict response from MelCloud
        """
        self._headers.set('content-type', "application/json; charset=UTF-8")
        return self._web_cmd(self._web.post_jsn, url, self._headers.all, data)

    def _web_cmd_get(self, url:str) -> dict:
        """
        Get dict from specified url
        This method is a convenience function, it calls the universal _web_cmd with
        the desired Web transport method (static)
        :param url: URL to access
        :return: dict response from MelCloud
        """
        self._headers.delete('content-type')
        return self._web_cmd(self._web.get_jsn, url, self._headers.all)

    def _web_cmd(self, webfunc, url, headers, data=None):
        """
        Universal web command which calls the Web transport. It handles known exceptions
        and initiates a auto-re-login if a 401 response is received.
        :param webfunc: static method of Web transport
        :param url: URL to access
        :param headers: headers dictionary
        :param data: optional data, used for post actions
        :return: dict response from MelCloud
        """

        if isinstance(data, dict):
            send_data = json.dumps(data).replace("None", "null")
        else:
            send_data = data

        try:
            if self._context_key is not None:
                # first time use
                if data is None:
                    return webfunc(url, headers)
                else:
                    return webfunc(url, headers, data=send_data)
        except Exception as e:
            # we dont expect any other error than 401
            if not isinstance(e, WebErr.WebExceptionAuth):
                print(e)
                raise ApiErr.APIExceptionCommError

        # received a 401 error, we need to re-authenticate to update
        # the context key
        self._log.print("(Re-)Login")
        if not self._login():
            # failure of re-login cannot be recovered
            raise ApiErr.APIExceptionCommError
        try:
            # attempt operation after sucessfull re-login
            if data is None:
                return webfunc(url, headers)
            else:
                return webfunc(url, headers, data=data)
        except:
            raise ApiErr.APIExceptionCommError

    @property
    def building(self) -> dict:
        """
        Provides the building structure dict from MelCloud. Only one building is supported yet.
        The building information is only fetched once as the data is assumed to be static for
        the purpose of this application.
        :return: cached or fetched building dict from MelCloud
        """
        if self._cached_building is None:
            self._cached_building = self._web_cmd_get(self._urls.list_devices)
        return self._cached_building

    def get_device(self, bld_id:int, dev_id:int) -> dict:
        """
        Fetches the specified device structure from MelCloud
        :param bld_id: building id
        :param dev_id: device id
        :return: device dict from MelCloud
        """
        self._log.print("get_device bld_id=%d dev_id=%d" % (bld_id, dev_id))
        url_cmd = self._urls.dev_status(dev=dev_id, bld=bld_id)
        response = self._web_cmd_get(url_cmd)
        return response

    def apply(self, obj) -> None:
        """
        Sends the provided object to MelCloud for update. Once the object has been recieved
        by MelCloud, the current object is sent back as a response.
        :param obj: object to send, only MelDevice allowed currently
        :return: response object as dic
        """
        if isinstance(obj, MelDevice):
            current_devstate = self._web_cmd_post(self._urls.set_dev, obj.Dict)
            # update the device state
            obj.Dict = current_devstate
            return
        raise ValueError("unsupported type to apply")

    def udpate(self, obj) -> None:
        """
        Updates the specified object from MelCloud. The stored state in obj is completely
        overwritten.
        :param obj: object to update, only MelDevice allowed currently
        :return: response object as dic
        """
        if isinstance(obj, MelDevice):
            url_cmd = self._urls.dev_status(dev=obj.ID, bld=obj.BuildingID)
            current = self._web_cmd_get(url_cmd)
            # update the device state
            obj.Dict = current
            return
        raise ValueError("unsupported type to apply")
