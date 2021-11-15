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

class Urls:
    _dev_status = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/Get?"

    @property
    def login(self):
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/Login/ClientLogin"

    @property
    def list_devices(self):
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/User/ListDevices"

    @property
    def set_dev(self):
        return "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/SetAta"

    def dev_status(self, bld, dev):
        return self._dev_status + "id=%d&buildingID=%d" % (dev, bld)
