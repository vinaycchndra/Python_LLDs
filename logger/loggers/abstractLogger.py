from ABC import abstractmethod
from loggerSubject import LoggerSubject


class AbstractLogger:
    __my_log_level = None

    def setNextLogger(self, next_level_logger):
        self.next_level_logger = next_level_logger

    def logMessage(self, log_level : int, log_message: str = "", logger_subject: LoggerSubject = None): 
        if log_level == self.__my_log_level:
            logger_subject.routeMessage(log_level, logger_subject)

        if self.next_level_logger is not None:
            self.next_level_logger.logMessage(log_level, log_message, logger_subject)


        