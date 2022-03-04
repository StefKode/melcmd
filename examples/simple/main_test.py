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
import sys
import os
from os.path import dirname
sys.path.append(dirname(__file__) + os.sep + ".." + os.sep + "..")

from factory.default import DefaultFactory
from config.config_mel import ConfigMel as Config

from util import log
log.trace_enable = False

config = Config("config.json")
make = DefaultFactory()
building = make.MelBuilding()
api = make.MelAPI(username=config.username,
                  password=config.password)

print("USE IMPLICIT LOGIN")

print("UPDATE DEVICE DETAILS")
building.update(api.building)
print("BuildingID = %d" % building.ID)

devices = {}
for dev_id in building.device_ids:
    data = api.get_device(building.ID, dev_id)
    name = building.id_to_name(dev_id)
    dev = make.MelDevice(fac=make, bld_id=building.ID, data=data, id=dev_id, name=name)
    devices[name] = dev
    print("DeviceName = " + dev.Name)
    print("    ID     = %d" % dev.ID)
    print("    Power  = %s" % str(dev.Power))
    print("   RoomTemp= %f" % dev.RoomTemperature)
    print("    SetTemp= %f" % dev.SetTemperature)
    dev.Power = False
    api.apply(dev)


