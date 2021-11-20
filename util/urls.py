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
from util.urls_base import UrlsBase


class Urls(UrlsBase):
    """Class to provide endpoint urls for MelCloud"""
    _dev_status = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/Get?"

    @property
    def login(self) -> str:
        """
        Provides login URL
        :return: login url string
        """
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/Login/ClientLogin"

    @property
    def list_devices(self) -> str:
        """
        Provides url to list all devices (get building dict)
        :return: building url string
        """
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/User/ListDevices"

    @property
    def set_dev(self) -> str:
        """
        Provides url to update a device in MelCloud
        :return: device update url string
        """
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/SetAta"

    def dev_status(self, bld:int, dev:int) -> str:
        """
        Provides custom url to fetch device status with encoded building and device id
        :param bld: building id
        :param dev: device id
        :return: device url string
        """
        return self._dev_status + "id=%d&buildingID=%d" % (dev, bld)
