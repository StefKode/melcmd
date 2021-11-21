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
from factory.factory_base import MelBaseFactory
from device.mel_device_base import MelDeviceBase


class MelDevice(MelDeviceBase):
    def __init__(self, fac:MelBaseFactory, data:dict, id:int, name:str):
        self._make = fac
        self._data = data
        self._id = id
        self._name = name
        self._log = self._make.Log("MelDev(%d)" % id)

    @property
    def ID(self) -> int:
        return self._id

    @property
    def Name(self) -> str:
        return self._name

    @property
    def Power(self) -> bool:
        return self._data['Power']

    @Power.setter
    def Power(self, state):
        self._data['Power'] = state
        self._data['EffectiveFlags'] = 1
        self._data['HasPendingCommand'] = True

    @property
    def Dict(self) -> dict:
        return self._data