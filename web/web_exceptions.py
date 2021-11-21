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


class WebExceptionAuth(Exception):
    """Custom HTTP authentication exception"""
    pass


class WebExceptionConnection(Exception):
    """Custom HTTP connection error exception"""
    pass


class WebExceptionNotFound(Exception):
    """Custom HTTP resource not found exception"""
    pass


class WebExceptionMisc(Exception):
    """Custom HTTP unknown error exception"""
    pass


class WebException_JsnDecode(Exception):
    """Custom HTTP response Json decoder error exception"""
    pass
