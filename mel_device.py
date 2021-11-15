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
    def __init__(self, data, id, name, set_update):
        self._data = data
        self._id = id
        self._name = name
        self._set_update = set_update
        self.log = Log("MelDev(%d)" % id)

    @property
    def ID(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @property
    def Power(self):
        return self._data['Power']

    @Power.setter
    def Power(self, state):
        self._data['Power'] = state
        self._data['EffectiveFlags'] = 1
        self._data['HasPendingCommand'] = True
        self._set_update(self._data)

