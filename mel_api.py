from web_transport import WebCmd as Web
import web_exceptions as WebErr
import mel_api_exceptions as ApiErr
from html_headers import Headers
from mel_device import MelDevice
from urls import Urls
from log import Log

class MelAPI:
    en_log = False
    context_key = None
    LOG_INFO = 0
    LOG_ERR = 1
    cached_building = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = Headers()
        self.urls = Urls()
        self.log = Log("MelAPI")

    def login(self) -> bool:
        login = '{"Email":"%s"' % self.username
        login += ',"Password":"%s"' % self.password
        login += ',"Language":4,"AppVersion":"1.22.8.0",'
        login += '"Persist":false,"CaptchaResponse":null}'
        self.log.print("start login")
        self.headers.delete('x-mitscontextkey')
        self.headers.set('content-type', "application/json; charset=UTF-8")
        try:
            response = Web.post_jsn(url=self.urls.login,
                                    headers=self.headers.all,
                                    data=login)
        except Exception as e:
            print(e)
            self.context_key = None
            return False

        self.context_key = response['LoginData']['ContextKey']
        self.log.print("ContextKey = " + str(self.context_key))
        self.headers.set('x-mitscontextkey', self.context_key)
        self.headers.delete('content-type')
        return True

    @property
    def building(self) -> dict:
        if self.cached_building is None:
            if self.context_key is None:
                return False
            self.cached_building = Web.get_jsn(self.urls.list_devices,
                                               headers=self.headers.all)
        return self.cached_building

    def get_device(self, bld_id, dev_id) -> dict:
        try:
            return self._get_device(bld_id, dev_id)
        except Exception as e:
            if type(e) != WebErr.WebException_Auth:
                print(e)
                raise ApiErr.API_CommError

        self.log.print("Re-Login", Log.ERR)
        if not self.login():
            raise ApiErr.API_CommError
        try:
            return self._get_device(bld_id, dev_id)
        except:
            raise ApiErr.API_CommError

    def _get_device(self, bld_id, dev_id):
        self.log.print("get_device bld_id=%d dev_id=%d" % (bld_id, dev_id))
        url_cmd = self.urls.dev_status(dev=dev_id,
                                       bld=bld_id)

        self.log.print("update_device url=%s" % url_cmd)
        response = Web.get_jsn(url_cmd, headers=self.headers.all)
        self.log.print("update_device resp=%s" % str(response))

        return response

    def apply(self, dev:MelDevice) -> None:
        try:
            self._apply(dev.Dict)
            return
        except Exception as e:
            if type(e) != WebErr.WebException_Auth:
                print(e)
                raise ApiErr.API_CommError

        self.log.print("Re-Login", Log.ERR)
        if not self.login():
            raise ApiErr.API_CommError
        try:
            self._apply(dev.Dict)
        except:
            raise ApiErr.API_CommError

    def _apply(self, dict):
        response = Web.post_jsn(self.urls.set_dev,
                                headers=self.headers.all,
                                data=dict)
        return response
