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

#
# This sample application monitors all Mel Devices. If they get turned on, then this
# tool turns them off after approximately 30min
#
from factory.default import DefaultFactory
from config.config import Config
from datetime import datetime
import time

RUNTIME_SEC=30*60
CHECK_TIME_SEC=5*60


def time_str():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S : ")


def report(text):
    print(time_str() + str(text))


config = Config("config.json")
make = DefaultFactory()
building = make.MelBuilding()
api = make.MelAPI(username=config.username, password=config.password)

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
    print("    Power  = %s" % str(dev.Power))

print("MONITOR DEVICES")
report("started")
while True:
    for devname in devices:
        dev = devices[devname]
        api.udpate(dev)

        if not dev.Power:
            dev.last_power = False
            continue

        if dev.Power and not dev.last_power:
            report("%s was turned ON, start tracking" % devname)
            dev.last_ts = datetime.now()
            dev.last_power = dev.Power
            continue

        if dev.Power and dev.last_power:
            duration = (datetime.now() - dev.last_ts).total_seconds()
            report("%s has left: %d min" % (devname, round((RUNTIME_SEC-duration)/60)))
            if duration > RUNTIME_SEC:
                report("%s turn OFF" % devname)
                dev.Power = False
                api.apply(dev)
                dev.last_power = False
            continue

        print("BUG")
    time.sleep(CHECK_TIME_SEC)
