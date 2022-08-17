import logging.handlers

class SysLogServer:


    host = 'syslog.fipo.com.br'

    def __init__(self) -> None:
        self._graylog = logging.handlers.SysLogHandler(self.host)
        
    @property
    def graylog(self):
        return self._graylog