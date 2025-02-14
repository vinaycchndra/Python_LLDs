from loggerEnum import LogLevel

# Sample configuration file
# sample_conf = {
#                     "global_log_level": LogLevel.DEBUG, 
#                     "file_handler": 
#                                 {"file_name": "app.log", "log_level": LogLevel.INFO}, 
#                     "stream_handler": {"log_level": LogLevel.INFO}
#             }

class Logger: 
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls) 
        return cls.__instance
    
    def __init__(self, conf: dict = None): 
        self.__conf = conf
        self.__default_conf = {
                            
                            "global_log_level": LogLevel.DEBUG, 
                            "file_handler": None, 
                            "stream_handler": {"log_level": LogLevel.INFO}
                        }
        
        if self.__conf:
            # Create logger with default configuration.
            pass        
        
    def getLogger(self):
        return self.__instance
    
obj = Logger("value")
print(obj.get_instance())

