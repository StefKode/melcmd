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
from factory.factory_base import MelBaseFactory


class MelDeviceBase():
    @abstractmethod
    def __init__(self, fac:MelBaseFactory,data:dict, id:int, name:str):
        """
        :param fac: factory to use
        :param data: dictionary with MelCloud device structure
        :param id: id of the device
        :param name: name of the device
        """

    @abstractmethod
    @property
    def ID(self) -> int:
        """
        :return: id of device
        """

    @abstractmethod
    @property
    def Name(self) -> str:
        """
        :return: name of device
        """

    @abstractmethod
    @property
    def Power(self) -> bool:
        """
        :return: power state of device
        """

    @abstractmethod
    @Power.setter
    def Power(self, state) -> None:
        """
        :param state: target power state of the device
        """

    @abstractmethod
    @property
    def Dict(self) -> dict:
        """
        :return: state dict of device
        """