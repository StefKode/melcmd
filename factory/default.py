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
from api.mel_api import MelAPI
from web.web_transport import WebTransport
from building.mel_building import MelBuilding
from device.mel_device import MelDevice
from util.urls import Urls
from util.log import Log


class DefaultFactory(MelCmdFactory):
    def MelAPI(self, username:str, password:str) -> MelAPI:
        return MelAPI(self, username, password)

    def WebTransport(self) -> WebTransport:
        return WebTransport()

    def MelBuilding(self) -> MelBuilding:
        return MelBuilding(self)

    def MelDevice(self, fac, bld_id:int, data:dict, id:int, name:str) -> MelDevice:
        return MelDevice(fac=fac, bld_id=bld_id, data=data, id=id, name=name)

    def Urls(self) -> Urls:
        return Urls()

    def Log(self, name:str) -> Log:
        return Log(name)
