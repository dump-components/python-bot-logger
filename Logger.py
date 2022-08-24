import logging
from SysLogServer import SysLogServer

class Logger:


    def __init__(self, user: logging.Logger, syslog_host=None) -> None:
        self._user = user
        self._basic_config(syslog_host)

    def info(self, message):
        self._loggin.info(f"{self._user} {message}")
        return message

    def debug(self, message):
        self._loggin.debug(f"{self._user} {message}")
        return message
    
    def warning(self, message):
        self._loggin.warning(f"{self._user} {message}")
        return message

    def error(self, message):
        self._loggin.error(f"{self._user} {message}")
        return message

    def critical(self, message):
        self._loggin.critical(f"{self._user} {message}")
        return message

    def _basic_config(self, syslog_host: str):
        logger = logging
        self._loggin = logger.getLogger(self._user)
        log_format = '%(asctime)s:%(levelname)s:%(message)s'
        logger.basicConfig(format=log_format, level=logger.DEBUG, filename=f'./logs/bot.log', filemode='w')
        if syslog_host:
            syslog_server = SysLogServer(syslog_host)
            self._loggin.addHandler(syslog_server.graylog)


