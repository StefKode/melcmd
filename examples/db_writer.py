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
import sys
import os
from os.path import dirname
sys.path.append(dirname(__file__) + os.sep + "..")
from examples.db_config import ConfigDB
import psycopg2


class DbWriter:
    def __init__(self, config: ConfigDB):
        self._conf = config
        self.conn = None
        self._cur = None
        self._connect()

    def _connect(self):
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            connect_str = f"host={self._conf.host} port={self._conf.port} dbname={self._conf.db} user={self._conf.user} password={self._conf.password}"
            print(connect_str)
            self._conn = psycopg2.connect(connect_str)
            # create a cursor
            self._cur = self._conn.cursor()#
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def publish(self, id: int, power: bool, set_temp: float, room_temp: float):
        try:
            cmd = 'INSERT INTO %s (devid, power, set_temp, room_temp) VALUES (%d, \'%d\', %0.1f, %0.1f)' % \
                  (self._conf.table, id, power, set_temp, room_temp)
            #print(cmd)
            self._cur.execute(cmd)
            self._conn.commit()
        except Exception as e:
            print("hallo")
            print(e)
