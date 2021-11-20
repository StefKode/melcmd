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
from abc import abstractmethod
from factory.factory_base import MelBaseFactory

class MelAPIBase:
    """Provides access to functions of the MelCloud"""

    @abstractmethod
    def __init__(self, fac:MelBaseFactory, username:str, password:str):
        """
        Constructor of API object. The login credentials cannot be updated after creation.
        :param fac: reference to factory
        :param username: username string
        :param password: password string
        """

    @abstractmethod
    def _login(self) -> bool:
        """
        Login to MelCloud using username and password properties
        The login session is represented by the context_key property.
        Login() can be called any time again.
        This function does not throw any expected exception, instead it returns False
        if such an exception is
        :return: True if login was successful, False if otherwise.
        """

    @abstractmethod
    def _web_cmd_post(self, url:str, data:dict):
        """
        Post a dictionary (data) to the specified url
        This method is a convenience function, it calls the universal _web_cmd with
        the desired Web transport method (static)
        :return: dict response from MelCloud
        """

    @abstractmethod
    def _web_cmd_get(self, url:str) -> dict:
        """
        Get dict from specified url
        This method is a convenience function, it calls the universal _web_cmd with
        the desired Web transport method (static)
        :param url: URL to access
        :return: dict response from MelCloud
        """

    @abstractmethod
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

    @abstractmethod
    @property
    def building(self) -> dict:
        """
        Provides the building structure dict from MelCloud. Only one building is supported yet.
        The building information is only fetched once as the data is assumed to be static for
        the purpose of this application.
        :return: cached or fetched building dict from MelCloud
        """

    @abstractmethod
    def get_device(self, bld_id:int, dev_id:int) -> dict:
        """
        Fetches the specified device structure from MelCloud
        :param bld_id: building id
        :param dev_id: device id
        :return: device dict from MelCloud
        """

    @abstractmethod
    def apply(self, obj) -> dict:
        """
        Sends the provided object to MelCloud for update. Once the object has been recieved
        by MelCloud, the current object is sent back as a response.
        :param obj: object to send, only MelDevice allowed currently
        :return: response object as dic
        """
