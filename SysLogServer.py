import logging.handlers

class SysLogServer:


    def __init__(self, syslog_host: str) -> None:
        self.__host = syslog_host
        self.__graylog = logging.handlers.SysLogHandler(self.__host)
        
    @property
    def graylog(self):
        return self.__graylog