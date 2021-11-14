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
from log import Log

class MelDevice():
    def __init__(self, data, id, name):
        self._data = data
        self._id = id
        self._name = name
        self.log = Log("MelDev(%d)" % id)

    def ID(self):
        return self._id

    def Name(self):
        return self._name

    def isPower(self):
        return self._data['Power']

    def set_power_state(self, state):
        self._data['Power'] = state
        self._data['EffectiveFlags'] = 1
        self._data['HasPendingCommand'] = True

    def to_dict(self):
        return self._data
