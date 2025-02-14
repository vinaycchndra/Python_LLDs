from abstractLogger import  AbstractLogger
from loggerEnum import LogLevel

class InfoLogger(AbstractLogger):
    
    def __init__(self):
        self.__my_log_level = LogLevel.INFO
        self.next_level_logger = None

    def __routeMessage(self, message, logger_subject):
        logger_subject.notify_all_observers(self.__my_log_level,  "Info : "+message)