from loggerEnum import LogLevel

class LoggerSubject: 
    def __init__(self):
        self._log_level_to_log_observers = { 
                                                LogLevel.CRITICAL: [], 
                                                LogLevel.DEBUG: [],
                                                LogLevel.ERROR: [], 
                                                LogLevel.INFO: [],
                                                LogLevel.WARNING: []     
                                        }
        
    def addObserver(self, log_level: str, log_observer):
        log_level_observer_list = self._log_level_to_log_observers.get(log_level)    
        is_observer_already_added = False

        for observer in log_level_observer_list:
            if observer == log_observer:
                is_observer_already_added = True
        
        if not is_observer_already_added:
            log_level_observer_list.append(log_observer)

    def notify_all_observers(self, log_level, message: str): 
        log_level_observer_list = self._log_level_to_log_observers.get(log_level) or []  
        
        for observer in log_level_observer_list: 
            observer.log(message)