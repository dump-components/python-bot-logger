import logging
from SysLogServer import SysLogServer

class Logger:


    def __init__(self, user: logging.Logger, syslog_host=None) -> None:
        self.__user = user
        self.__logger = self._basic_config(syslog_host)

    def info(self, message):
        self.__logger.info(f"{message}")
        return message

    def debug(self, message):
        self.__logger.debug(f"{message}")
        return message
    
    def warning(self, message):
        self.__logger.warning(f"{message}")
        return message

    def error(self, message):
        self.__logger.error(f"{message}")
        return message

    def critical(self, message):
        self.__logger.critical(f"{message}")
        return message

    def _basic_config(self, syslog_host: str):
        logger = logging.getLogger(self.__user)
        log_format = '%(message)s'
        logging.basicConfig(format=log_format, level=logging.DEBUG, filename=f'./logs/bot.log', filemode='w')
        if syslog_host:
            logger.addHandler(SysLogServer(syslog_host).graylog)
        return logger


