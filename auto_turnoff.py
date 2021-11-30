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
from device.mel_device import MelDevice
from config.config import Config
from datetime import datetime
import time


##########################################################################################
# configuration of the tracking
RUNTIME_SEC=30*60
CHECK_TIME_SEC=5*60


##########################################################################################
# Tailor classes for Tracking purpose
class TrackingDevice(MelDevice):
    last_ts = None
    last_power = False


class TrackingFactory(DefaultFactory):
    # overwrite device maker to deliver TrackingDevice
    def MelDevice(self, fac, bld_id:int, data:dict, id:int, name:str) -> TrackingDevice:
        return TrackingDevice(fac=fac, bld_id=bld_id, data=data, id=id, name=name)



def time_str():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S : ")


def report(text):
    print(time_str() + str(text))


config = Config("config.json")
make = TrackingFactory()
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
            report("%s Room %3.1f°C" % (devname, dev.RoomTemperature))
            dev.last_power = False
            continue

        if dev.Power and not dev.last_power:
            report("%s was turned ON, start tracking" % devname)
            dev.last_ts = datetime.now()
            dev.last_power = dev.Power
            continue

        if dev.Power and dev.last_power:
            duration = (datetime.now() - dev.last_ts).total_seconds()
            report("%s (%3.1f°C) has left: %d min" % (devname, dev.RoomTemperature, round((RUNTIME_SEC-duration)/60)))
            if duration > RUNTIME_SEC:
                if dev.RoomTemperature < dev.SetTemperature:
                    report("%s timeout but wait for settemp to settle (%3.1f°C)" %
                           (devname, dev.SetTemperature - dev.RoomTemperature))
                report("%s turn OFF" % devname)
                dev.Power = False
                api.apply(dev)
                dev.last_power = False
            continue

        print("BUG")
    time.sleep(CHECK_TIME_SEC)

