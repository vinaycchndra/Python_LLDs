from .abstractLogger import  AbstractLogger
from loggerEnum import LogLevel

class ErrorLogger(AbstractLogger):
    
    def __init__(self):
        self._my_log_level = LogLevel.ERROR
        self.next_level_logger = None

    def routeMessage(self, message, logger_subject):
        logger_subject.notify_all_observers(self._my_log_level,  "Error : "+message)