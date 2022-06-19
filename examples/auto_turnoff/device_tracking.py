from device.mel_device import MelDevice
from api.mel_api import MelAPI
from datetime import datetime


class TrackingDevice(MelDevice):
    _last_ts = None
    _last_power = False
    _RUNTIME_SEC = 45 * 60

    def setRuntime(self, time):
        self._RUNTIME_SEC = time

    def evaluate(self, api: MelAPI, report, timelimit=True):
        api.udpate(self)
        if not self.Power:
            report("%s Room %3.1f°C" % (self.Name, self.RoomTemperature))
            self._last_power = False
            return

        if self.Power and not self._last_power:
            report("%s was turned ON, start tracking" % self.Name)
            self._last_ts = datetime.now()
            self._last_power = self.Power
            return

        if self.Power and self._last_power:
            duration = (datetime.now() - self._last_ts).total_seconds()
            report("%s (%3.1f°C) has left: %d min" % (self.Name,
                                                      self.RoomTemperature,
                                                      round((self._RUNTIME_SEC-duration)/60)))

            if timelimit:
                report("%s timelimit enabled" % self.Name)
                if duration > self._RUNTIME_SEC:
                    if self.RoomTemperature < self.SetTemperature:
                        report("%s timeout but wait for settemp to settle (%3.1f°C)" %
                               (self.Name, self.SetTemperature - self.RoomTemperature))
                    report("%s turn OFF" % self.Name)
                    self.Power = False
                    api.apply(self)
                    self._last_power = False
                else:
                    report("%s timelimit disabled" % self.Name)
            return
