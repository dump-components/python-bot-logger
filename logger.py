from loguru import logger
from sys import stderr

class Logger:

    def __init__(self) -> None:
        logger.add(
            sink=stderr,
            filter=self._send_email_if_critical,
            format='{time} {level} {message}',
            level='INFO'
        )

    def _send_email_if_critical(self, decoder):
        if decoder['level'] == 'CRITICAL':
            print("função enviou email por smtp")

    def info(self, message):
        logger.info(message)
        return message

    def debug(self, message):
        logger.debug(message)
        return message
    
    def warning(self, message):
        logger.warning(message)
        return message

    def error(self, message):
        logger.error(message)
        return message

    def critical(self, message):
        logger.critical(message)
        return message

