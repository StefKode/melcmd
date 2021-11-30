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

from web import web_exceptions as Error
import requests
import json


class WebTransport:
    """
    Static class which provides http post and get functions. It translates certain
    http error codes into specific exceptions (web_exception)
    """

    @staticmethod
    def post_jsn(url, headers: dict, data: dict) -> dict:
        """
        Perform HTTP POST operation. Any returned data is assumed to be Json and will be
        converted to a dictionary. Any response other Json will return in exception.
        :param url: URL to use
        :param headers: header dict to use
        :param data: data dict to use
        :return: dict response
        """
        ret_data = None
        try:
            r = requests.post(url, headers=headers, data=data)
        except Exception as e:
            #print(e)
            raise Error.WebExceptionConnection

        if r.status_code == 401:
            raise Error.WebExceptionAuth
        if r.status_code == 404:
            raise Error.WebExceptionNotFound
        if r.status_code != 200:
            raise Error.WebExceptionMisc

        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            raise Error.WebException_JsnDecode

    @staticmethod
    def get_jsn(url, headers: dict) -> dict:
        """
        Perform HTTP GET operation. Any returned data is assumed to be Json and will be
        converted to a dictionary. Any response other Json will return in exception.
        :param url: URL to use
        :param headers: header dict to use
        :return: dict response
        """
        ret_data = None
        try:
            r = requests.get(url, headers=headers)
        except Exception as e:
            #print(e)
            raise Error.WebExceptionConnection

        if r.status_code == 401:
            raise Error.WebExceptionAuth
        if r.status_code == 404:
            raise Error.WebExceptionNotFound
        if r.status_code != 200:
            raise Error.WebExceptionMisc

        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            raise Error.WebException_JsnDecode
