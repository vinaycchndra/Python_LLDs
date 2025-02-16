from loggerEnum import LogLevel
from loggers import criticalLogger, debugLogger, warningLogger, errorLogger, infoLogger
from logObservers import consoleLogger, fileLogger

class LogManager:
    
    @classmethod
    def createChainOfResponsibility(cls, conf):
        info_logger = infoLogger.InfoLogger()
        warning_logger = warningLogger.WarningLogger()
        debug_logger = debugLogger.DebugLogger()
        error_logger = errorLogger.ErrorLogger()
        critical_logger = criticalLogger.CriticalLogger()
        logger_chain = debug_logger

        # making logger chain
        debug_logger.setNextLogger(info_logger)
        info_logger.setNextLogger(warning_logger)
        warning_logger.setNextLogger(error_logger)
        error_logger.setNextLogger(critical_logger)
        
        global_log_level = conf.get("global_log_level", None)

        if global_log_level:
            if  isinstance(global_log_level, LogLevel) is False:
                raise Exception("Not a valid log level type is given as input.")
            
            while logger_chain.get_log_level() != global_log_level:
                logger_chain = logger_chain.next_level_logger
        return logger_chain
    
    @classmethod
    def configureLogObservers(cls, conf: dict, logger_subject): 
        
        # Adding file handler
        file_handler_conf = conf.get("file_handler", {})
        
        if len(file_handler_conf)>0:
            log_file_add = file_handler_conf.get("file_address", "./app.log")
            file_log_level = file_handler_conf.get("log_level") or conf.get("global_log_level") or LogLevel.DEBUG
            
            if  isinstance(file_log_level, LogLevel) is False:
                raise Exception("Not a valid log level type is given as input for file handler.")

            file_logger = fileLogger.FileLogger(file_address=log_file_add)
            
            for log_level in LogLevel:
                if log_level.value >= file_log_level.value:
                    logger_subject.addObserver(log_level, file_logger)
            
        # Adding console logger
        console_handler_conf = conf.get("console_handler", {})
        console_logger = consoleLogger.ConsoleLogger()

        if len(console_handler_conf) >= 0:
            console_log_level = console_handler_conf.get("log_level") or conf.get("global_log_level") or LogLevel.DEBUG
            if  isinstance(console_log_level, LogLevel) is False:
                raise Exception("Not a valid log level type is given as input for console handler.")
        else:
            console_log_level = console_handler_conf.get("log_level") or conf.get("global_log_level") or LogLevel.DEBUG

        
        for log_level in LogLevel:
            if log_level.value >= console_log_level.value:
                logger_subject.addObserver(log_level, console_logger)
        

        

    
