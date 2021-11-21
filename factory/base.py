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
from abc import abstractmethod


class MelCmdFactory:
    @abstractmethod
    def MelAPI(self, *args):
        pass

    @abstractmethod
    def WebTransport(self):
        pass

    @abstractmethod
    def MelBuilding(self):
        pass

    @abstractmethod
    def MelDevice(self, *args):
        pass

    @abstractmethod
    def Urls(self):
        pass

    @abstractmethod
    def Log(self, *args):
        pass