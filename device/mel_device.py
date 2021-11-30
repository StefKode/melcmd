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
from factory.base import MelCmdFactory
from device.mel_device_base import MelDeviceBase


class MelDevice(MelDeviceBase):
    def __init__(self, fac:MelCmdFactory, bld_id:int, data:dict, id:int, name:str):
        self._make = fac
        self._bld = bld_id
        self._data = data
        self._id = id
        self._name = name
        self._log = self._make.Log("MelDev(%d)" % id)

    @property
    def ID(self) -> int:
        return self._id

    @property
    def BuildingID(self) -> int:
        return self._bld

    @property
    def Name(self) -> str:
        return self._name

    @property
    def RoomTemperature(self) -> float:
        return self._data['RoomTemperature']

    @property
    def SetTemperature(self) -> float:
        return self._data['SetTemperature']

    @SetTemperature.setter
    def SetTemperature(self, value: float):
        if not isinstance(value, float):
            raise TypeError
        self._data['SetTemperature'] = round(value * 2)/2
        self._data['EffectiveFlags'] = 1
        self._data['HasPendingCommand'] = True

    @property
    def Power(self) -> bool:
        return self._data['Power']

    @Power.setter
    def Power(self, state:bool):
        self._data['Power'] = state
        self._data['EffectiveFlags'] = 1
        self._data['HasPendingCommand'] = True

    @property
    def Dict(self) -> dict:
        return self._data

    @Dict.setter
    def Dict(self, state:dict):
        self._data = state
