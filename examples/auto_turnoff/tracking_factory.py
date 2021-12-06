from examples.auto_turnoff.device_tracking import TrackingDevice
from factory.default import DefaultFactory


class TrackingFactory(DefaultFactory):
    # overwrite device maker to deliver TrackingDevice
    def MelDevice(self, fac, bld_id:int, data:dict, id:int, name:str) -> TrackingDevice:
        return TrackingDevice(fac=fac, bld_id=bld_id, data=data, id=id, name=name)