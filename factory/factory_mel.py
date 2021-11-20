from factory.factory_base import MelBaseFactory
from api.mel_api import MelAPI
from web.web_transport import WebTransport
from building.mel_building import MelBuilding
from device.mel_device import MelDevice
from util.urls import Urls
from util.log import Log


class MelFactory(MelBaseFactory):
    def make_api(self, username:str, password:str) -> MelAPI:
        return MelAPI(self, username, password)

    def make_web_transport(self) -> WebTransport:
        return WebTransport()

    def make_building(self) -> MelBuilding:
        return MelBuilding(self)

    def make_device(self, data:dict, id:int, name:str) -> MelDevice:
        return MelDevice(self, data, id, name)

    def make_url(self) -> Urls:
        return Urls()

    def make_log(self, name:str) -> Log:
        return Log(name)
