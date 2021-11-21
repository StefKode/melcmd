from abc import abstractmethod


class MelBaseFactory:
    @abstractmethod
    def MelAPI(self, *args):
        pass

    @abstractmethod
    def WebTransport(self):
        pass

    @abstractmethod
    def MelBuilding(self):
        pass

    @abstractmethod
    def MelDevice(self, *args):
        pass

    @abstractmethod
    def Urls(self):
        pass

    @abstractmethod
    def Log(self, *args):
        pass
