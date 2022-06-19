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
from config.config_base import ConfigBase


class ConfigDB(ConfigBase):
    @property
    def host(self):
        return self._config['host']

    @property
    def port(self):
        return self._config['port']

    @property
    def db(self):
        return self._config['db']

    @property
    def table(self):
        return self._config['table']

    @property
    def user(self):
        return self._config['user']

    @property
    def password(self):
        return self._config['password']

    @property
    def redis_host(self):
        return self._config['redis-host']

    @property
    def redis_prefix(self):
        return self._config['redis-prefix']

    @property
    def redis_aclimit_key(self):
        return self._config['redis-aclimit-key']
