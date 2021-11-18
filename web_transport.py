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
import web_exceptions as Error
import requests
import json

tmp = 0

class WebCmd:
    @staticmethod
    def post_jsn(url, headers, data):
        global tmp
        ret_data = None
        try:
            r = requests.post(url, headers=headers, data=data)
        except Exception as e:
            print(e)
            raise Error.WebException_Connection

        if r.status_code == 401:
            raise Error.WebException_Auth
        if r.status_code == 404:
            raise Error.WebException_NotFound
        if r.status_code != 200:
            raise Error.WebException_Misc

        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            raise Error.WebException_JsnDecode

    @staticmethod
    def get_jsn(url, headers):
        ret_data = None
        try:
            r = requests.get(url, headers=headers)
        except Exception as e:
            print(e)
            raise Error.WebException_Connection

        if r.status_code == 401:
            raise Error.WebException_Auth
        if r.status_code == 404:
            raise Error.WebException_NotFound
        if r.status_code != 200:
            raise Error.WebException_Misc

        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            raise Error.WebException_JsnDecode
