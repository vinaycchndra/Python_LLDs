from abc import ABC, abstractmethod
from loggerSubject import LoggerSubject


class AbstractLogger(ABC):
    _my_log_level = None

    def setNextLogger(self, next_level_logger):
        self.next_level_logger = next_level_logger
        

    def logMessage(self, log_level, log_message: str = "", logger_subject: LoggerSubject = None): 
        
        if log_level == self._my_log_level:
            self.routeMessage(log_message, logger_subject)

        if self.next_level_logger is not None:
            self.next_level_logger.logMessage(log_level, log_message, logger_subject)
        
    @abstractmethod
    def routeMessage(self, message: str, logger_subject): 
        pass
        
    def get_log_level(self): 
        return self._my_log_level