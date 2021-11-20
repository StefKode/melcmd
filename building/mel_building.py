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
from util.log import Log
from factory.factory_base import MelBaseFactory
from building.mel_building_base import MelBuildingBase


class MelBuilding(MelBuildingBase):
    _building_id = None
    _building_status = {}

    def __init__(self, fac:MelBaseFactory):
        self.factory = fac
        self.log = self.factory.make_log("MelBuilding")

    def update(self, status):
        self.log.print("update_building %s" % str(status))
        self._building_status = status
        self._building_id = self._building_status[0]['ID']

    @property
    def ID(self):
        return self._building_id

    @property
    def device_ids(self):
        for e in self._building_status:
            for d in e['Structure']['Devices']:
                yield d['DeviceID']

    def id_to_name(self, id):
        for e in self._building_status:
            for d in e['Structure']['Devices']:
                if d['DeviceID'] == id:
                    return d['DeviceName']
        return None


