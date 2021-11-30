from factory.default import DefaultFactory
from building.mel_building import MelBuilding
from api.mel_api import MelAPI

class DeviceManager:
    def __init__(self, make: DefaultFactory, api: MelAPI ,bld: MelBuilding):
        self._devices = {}
        for dev_id in bld.device_ids:
            data = api.get_device(bld.ID, dev_id)
            name = bld.id_to_name(dev_id)
            dev = make.MelDevice(fac=make, bld_id=bld.ID, data=data, id=dev_id, name=name)
            self._devices[name] = dev
            print("DeviceName = " + dev.Name)
            print("    Power  = %s" % str(dev.Power))

    @property
    def Devices(self):
        for dname in self._devices:
            yield self._devices[dname]
