#!/usr/bin/python3
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

import json
from urls import Urls
from html_headers import Headers
from web_cmd import WebCmd as Web

headers = Headers()
urls = Urls()

with open("config.json") as f:
    config = json.loads(f.read())

login = '{"Email":"%s"' % config['email']
login += ',"Password":"%s"' % config['password']
login += ',"Language":4,"AppVersion":"1.22.8.0","Persist":false,"CaptchaResponse":null}'

print("LOGIN")
response = Web.post_jsn(url=urls.login, headers=headers.get(), data=login)
if response is None:
    exit()

context_key = response['LoginData']['ContextKey']
print("ContextKey = " + str(context_key))
headers.set('x-mitscontextkey', context_key)
headers.delete('content-type')

print("LISTDEV")
response = Web.get_jsn(urls.list_devices, headers=headers.get())
if response is None:
    exit()

building_id = response[0]['ID']
print("BuildingID = " + str(building_id))

device_ids = {}
for e in response:
    for d in e['Structure']['Devices']:
        device_ids[d['DeviceName']] = d['DeviceID']
        print("DeviceName = " + str(d['DeviceName']))
        print("    ID     = " + str(d['DeviceID']))
        print("    Power  = " + str(d['Device']['Power']))

print("DEVICE STATUS")
dev_status = {}
for name in device_ids:
    url_cmd = urls.dev_status(dev=device_ids[name], bld=building_id)
    response = Web.get_jsn(url_cmd, headers=headers.get())
    if response is None:
        exit()
    dev_status[name] = response

exit()

print("START WZ")
device_name = "Wohnzimmer"
dev_id = device_ids[device_name]
dev_status[device_name]['Power'] = True
dev_status[device_name]['EffectiveFlags'] = 1
dev_status[device_name]['HasPendingCommand'] = True
response = Web.post_jsn(urls.set_dev, headers=headers.get(), data=dev_status[device_name])
dev_status[device_name] = response
