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
sys.path.append(dirname(__file__) + os.sep + "..")

#
# This sample application monitors all Mel Devices. If they get turned on, then this
# tool turns them off after approximately 30min
#
from config.config import Config
from device.device_mgr import DeviceManager
from datetime import datetime
import time

from examples.auto_turnoff_factory import TrackingFactory

##########################################################################################
# configuration of the tracking
RUNTIME_SEC=30*60
CHECK_TIME_SEC=5*60


##########################################################################################
# Console Logging
def time_str():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S : ")


def report(text):
    print(time_str() + str(text))


##########################################################################################
# initialize objects
config = Config("config.json")
make = TrackingFactory()
building = make.MelBuilding()
api = make.MelAPI(username=config.username, password=config.password)

##########################################################################################
# build device manager
print("UPDATE DEVICE DETAILS")
building.update(api.building)
print("BuildingID = %d" % building.ID)
devMgr = DeviceManager(make, api, building)

##########################################################################################
# Montoring
print("MONITOR DEVICES")
report("started")
while True:
    for dev in devMgr.Devices:
        dev.evaluate(api, report)
    time.sleep(CHECK_TIME_SEC)

