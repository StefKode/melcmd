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


class MelBuildingBase:
    @abstractmethod
    def __init__(self, fac:MelBaseFactory):
        """
        :param fac: factory to use
        """
    @abstractmethod
    def update(self, status):
        """
        :param status:
        :return:
        """

    @abstractmethod
    @property
    def ID(self):
        """

        :return:
        """

    @abstractmethod
    @property
    def device_ids(self):
        """

        :return:
        """

    @abstractmethod
    def id_to_name(self, id):
        """

        :param id:
        :return:
        """

