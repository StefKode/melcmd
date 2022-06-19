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

#
# This sample application monitors all Mel Devices. If they get turned on, then this
# tool turns them off after approximately 30min
#
from config.config_mel import ConfigMel
from device.device_mgr import DeviceManager
from datetime import datetime
import time

from examples.auto_turnoff.tracking_factory import TrackingFactory
from examples.auto_turnoff.db_config import ConfigDB
from examples.auto_turnoff.db_writer import DbWriter
from examples.auto_turnoff.rediscon import RedisCon

##########################################################################################
# configuration of the tracking
CHECK_TIME_SEC=5*60

DEBUG=True
USE_DB=True
USE_REDIS=True


##########################################################################################
# Console Logging
def time_str():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S : ")


def report(text):
    if not DEBUG:
        return
    print(time_str() + str(text))


##########################################################################################
# initialize objects
config = ConfigMel("config.json")
dbconf = ConfigDB("examples" + os.sep + "auto_turnoff" + os.sep + "dbconf.json")
make = TrackingFactory()
building = make.MelBuilding()
api = make.MelAPI(username=config.username, password=config.password)

if USE_DB:
    db = DbWriter(dbconf)
else:
    db = None

if USE_REDIS:
    red = RedisCon(name="acu", host=dbconf.redis_host, log_enabled=DEBUG, trx_log=DEBUG)
    red.setConMonInterval(5)
    red.connect()
else:
    red = None


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
        if USE_REDIS:
            timelimit = bool(red.get(dbconf.redis_aclimit_key))
            dev.evaluate(api, report, timelimit)
        else:
            dev.evaluate(api, report)

        if USE_DB:
            db.publish(dev.ID, dev.Power, dev.SetTemperature, dev.RoomTemperature)
        if USE_REDIS:
            if dev.Power:
                power_val = 1
            else:
                power_val = 0
            red.set("%s/%d/power"    % (dbconf.redis_prefix, dev.ID), power_val)
            red.set("%s/%d/setpoint" % (dbconf.redis_prefix, dev.ID), dev.SetTemperature)
    time.sleep(CHECK_TIME_SEC)

