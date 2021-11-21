from factory.factory_base import MelBaseFactory
from api.mel_api import MelAPI
from web.web_transport import WebTransport
from building.mel_building import MelBuilding
from device.mel_device import MelDevice
from util.urls import Urls
from util.log import Log


class MelFactory(MelBaseFactory):
    def MelAPI(self, username:str, password:str) -> MelAPI:
        return MelAPI(self, username, password)

    def WebTransport(self) -> WebTransport:
        return WebTransport()

    def MelBuilding(self) -> MelBuilding:
        return MelBuilding(self)

    def MelDevice(self, data:dict, id:int, name:str) -> MelDevice:
        return MelDevice(self, data, id, name)

    def Urls(self) -> Urls:
        return Urls()

    def Log(self, name:str) -> Log:
        return Log(name)
