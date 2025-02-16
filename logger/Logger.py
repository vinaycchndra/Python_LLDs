from logManager import LogManager
from loggerSubject import LoggerSubject
from loggerEnum import LogLevel

class Logger:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance  

    @classmethod
    def getLogger(cls, conf: dict = {}, reset = False): 
        if cls.__instance  is None or reset:
            cls.__instance = Logger()
            cls.__instance.__logger_chain = LogManager.createChainOfResponsibility(conf)
            cls.__instance.__logger_subject = LoggerSubject()
            LogManager.configureLogObservers(conf, cls.__instance.__logger_subject)

        return cls.__instance

    def info(self, msg: str):
        self.__logger_chain.logMessage(LogLevel.INFO, msg, self.__logger_subject)

    def debug(self, msg: str):
        self.__logger_chain.logMessage(LogLevel.DEBUG, msg, self.__logger_subject)

    def warning(self, msg: str):
        self.__logger_chain.logMessage(LogLevel.WARNING ,msg, self.__logger_subject)

    def error(self, msg: str):
        self.__logger_chain.logMessage(LogLevel.ERROR, msg, self.__logger_subject)

    def critical(self, msg: str):
        self.__logger_chain.logMessage(LogLevel.CRITICAL, msg, self.__logger_subject)
