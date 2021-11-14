from web_cmd import WebCmd as Web
from html_headers import Headers
from urls import Urls
from log import Log

class MelAPI:
    en_log = False
    context_key = None
    LOG_INFO = 0
    LOG_ERR = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = Headers()
        self.urls = Urls()
        self.log = Log("MelAPI")

    def login(self):
        login = '{"Email":"%s"' % self.username
        login += ',"Password":"%s"' % self.password
        login += ',"Language":4,"AppVersion":"1.22.8.0",'
        login += '"Persist":false,"CaptchaResponse":null}'
        self.log.print("start login")
        response = Web.post_jsn(url=self.urls.login,
                                headers=self.headers.get(),
                                data=login)
        if response is None:
            self.context_key = None
            return False

        self.context_key = response['LoginData']['ContextKey']
        self.log.print("ContextKey = " + str(self.context_key))
        self.headers.set('x-mitscontextkey', self.context_key)
        self.headers.delete('content-type')
        return True

    def get_building(self):
        if self.context_key is None:
            return False
        response = Web.get_jsn(self.urls.list_devices,
                               headers=self.headers.get())
        return response

    def get_device(self, bld_id, dev_id):
        self.log.print("get_device bld_id=%d dev_id=%d" % (bld_id, dev_id))
        url_cmd = self.urls.dev_status(dev=dev_id,
                                       bld=bld_id)

        self.log.print("update_device url=%s" % url_cmd)
        response = Web.get_jsn(url_cmd, headers=self.headers.get())
        self.log.print("update_device resp=%s" % str(response))

        return response

    def set_device(self, status):
        response = Web.post_jsn(self.urls.set_dev,
                                headers=self.headers.get(),
                                data=status)
        return response
