from abc import ABC, abstractmethod
from loggerSubject import LoggerSubject


class AbstractLogger(ABC):
    __my_log_level = None

    def setNextLogger(self, next_level_logger):
        self.next_level_logger = next_level_logger

    def logMessage(self, log_level : int, log_message: str = "", logger_subject: LoggerSubject = None): 
        if log_level == self.__my_log_level:
            self.__routeMessage(log_level, logger_subject)

        if self.next_level_logger is not None:
            self.next_level_logger.logMessage(log_message, logger_subject)
    
    @abstractmethod
    def __routeMessage(self, message: str, logger_subject): 
        pass
        