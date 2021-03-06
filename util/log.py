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
from util.log_base import LogBase
trace_enable = True

class Log(LogBase):
    TRACE = 0
    ERR = 1

    def __init__(self, who:str):
        self._who = who

    def print(self, text:str, level=TRACE):
        if level == self.ERR or trace_enable:
            print("%-15s: %s" % (self._who, str(text)))
