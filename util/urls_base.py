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


class UrlsBase:
    @abstractmethod
    @property
    def login(self) -> str:
        """
        Provides login URL
        :return: login url string
        """

    @abstractmethod
    @property
    def list_devices(self) -> str:
        """
        Provides url to list all devices (get building dict)
        :return: building url string
        """

    @abstractmethod
    @property
    def set_dev(self) -> str:
        """
        Provides url to update a device in MelCloud
        :return: device update url string
        """

    @abstractmethod
    def dev_status(self, bld:int, dev:int) -> str:
        """
        Provides custom url to fetch device status with encoded building and device id
        :param bld: building id
        :param dev: device id
        :return: device url string
        """
