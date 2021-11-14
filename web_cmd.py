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

import requests
import json


class WebCmd:
    @staticmethod
    def post_jsn(url, headers, data):
        ret_data = None
        try:
            r = requests.post(url, headers=headers, data=data)
            if r.status_code != 200:
                print("ERROR: bad status code " + str(r.status_code))
                print("URL: " + str(url))
                print("HEADERS: " + str(headers))
                return None
        except Exception as e:
            print(e)
            return None
        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_jsn(url, headers):
        ret_data = None
        try:
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                print("ERROR: bad status code " + str(r.status_code))
                print("URL: " + str(url))
                print("HEADERS: " + str(headers))
                return None
        except Exception as e:
            print(e)
            return None
        try:
            ret_data = json.loads(r.text)
            return ret_data
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def http_staus_string(value):
        if value == 200:
            return "OK"
        if value == 404:
            return "NOT FOUND"
        if value == 500:
            return "INTERNAL SERVER ERROR"

