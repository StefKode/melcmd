from abc import abstractmethod
from api.mel_api_base import MelAPIBase
from web.web_transport_base import WebTransportBase
from building.mel_building_base import MelBuildingBase
from device.mel_device_base import MelDeviceBase
from util.urls_base import UrlsBase
from util.log_base import LogBase


class MelBaseFactory:
    @abstractmethod
    def make_api(self, username:str, password:str) -> MelAPIBase:
        """
        :return: Mel API object
        """

    @abstractmethod
    def make_web_transport(self) -> WebTransportBase:
        """
        :return: Web Transport Base
        """

    @abstractmethod
    def make_building(self) -> MelBuildingBase:
        """
        :return: Web Building Base
        """

    @abstractmethod
    def make_device(self, data:dict, id:int, name:str) -> MelDeviceBase:
        """
        :return: Web Building Base
        """

    @abstractmethod
    def make_url(self) -> UrlsBase:
        """
        :return: Url object
        """

    @abstractmethod
    def make_log(self, name:str) -> LogBase:
        """
        :param name: name of logging source
        :return: Log object
        """
