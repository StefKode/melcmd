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
from util import log
import time
from factory.factory_mel import MelFactory

log.trace_enable = False

with open("config.json") as f:
    config = json.loads(f.read())

make = MelFactory()

building = make.MelBuilding()
api = make.MelAPI(username=config['email'],
                       password=config['password'])

print("USE IMPLICIT LOGIN")

print("UPDATE DEVICE DETAILS")
building.update(api.building)
print("BuildingID = %d" % building.ID)

devices = {}
for dev_id in building.device_ids:
    data = api.get_device(building.ID, dev_id)
    name = building.id_to_name(dev_id)
    dev = make.MelDevice(data, dev_id, name)
    devices[name] = dev
    print("DeviceName = " + dev.Name)
    print("    ID     = %d" % dev.ID)
    print("    Power  = %s" % str(dev.Power))

print("TEST")
wohnzimmer = devices['Wohnzimmer']
studio = devices['Studio']

print("STOP wz")
wohnzimmer.Power = False
api.apply(wohnzimmer)

print("WAIT 30min")
time.sleep(5)
api.headers.set("x-mitscontextkey", "1")

print("STOP again wz")
wohnzimmer.Power = False
api.apply(wohnzimmer)

print("DONE")