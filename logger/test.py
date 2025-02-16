import unittest
import io, sys, os
from Logger import Logger
from loggerEnum import LogLevel

class TestLoggerFramework(unittest.TestCase): 

    def test_unconfigured_console_logging(self):
        test_log_message = "Hi I am log message" 
        logger = Logger.getLogger(reset=True)
        console_output = io.StringIO()
        sys.stdout = console_output
        
        # console info log test
        logger.info(test_log_message)
        self.assertEqual(console_output.getvalue().strip(), "Info : "+test_log_message)
        
        # clearing the previous write on the string io
        console_output.seek(0)
        console_output.truncate(0)

        # console debug log test
        logger.debug(test_log_message)
        self.assertEqual(console_output.getvalue().strip(), "Debug : "+test_log_message)
        
        console_output.seek(0)
        console_output.truncate(0)

        # console warning log test
        logger.warning(test_log_message)
        self.assertEqual(console_output.getvalue().strip(), "Warning : "+test_log_message)

        console_output.seek(0)
        console_output.truncate(0)

        # console error log test
        logger.error(test_log_message)
        self.assertEqual(console_output.getvalue().strip(), "Error : "+test_log_message)

        console_output.seek(0)
        console_output.truncate(0)

        # console critical log test
        logger.critical(test_log_message)
        self.assertEqual(console_output.getvalue().strip(), "Critical : "+test_log_message)

        # resetting the stdio
        sys.stdout = sys.__stdout__

    def test_configured_console_file_logging(self):
        # creating a log file 
        file_address = "./test_app.log"
        test_conf = {
                    "global_log_level": LogLevel.DEBUG, 
                    "file_handler": 
                                {"file_address": file_address, "log_level": LogLevel.INFO}, 
                    "console_handler": {"log_level": LogLevel.WARNING}
            }
        logger = Logger.getLogger(conf=test_conf, reset=True)
        
        info_log = "I am info log !!!"
        debug_log =   "I am debug log !!!"      
        warning_log = "I am warning log !!!"
        error_log = "I am error log !!!"
        critical_log = "I am critical log !!!"
        
        
        console_output = io.StringIO()
        sys.stdout = console_output

        logger.debug(debug_log)
        logger.info(info_log)
        logger.warning(warning_log)
        logger.error(error_log)
        logger.critical(critical_log)

        # in the configuration json we have set the console handler log level to warning which means we should get at all logs from warning to critical 
        # in console and since we have set file_handler logs to info we should get all logs added to the file from the info to critical one more 
        # point we have set the global log level to dubug which should is lower in hierarchy from the console handler log level and file handler log level 
        # If we put something bigger than the hierarchy of the file handler or console handler than only those logs will only appear from the global_log_level
        # logs for the console and file handler logger.
        
        console_logs = console_output.getvalue()
        console_log_list = console_logs.strip().split("\n")
        self.assertEqual(console_log_list, ["Warning : "+warning_log, "Error : "+error_log, "Critical : "+critical_log])
        
        file_object = open(file_address, "r")
        file_log_list = [line.strip() for line in file_object.readlines()]
        self.assertEqual(file_log_list,  ["Info : "+info_log, "Warning : "+warning_log, "Error : "+error_log, "Critical : "+critical_log])

        file_object.close()
        # resetting the stdio
        sys.stdout = sys.__stdout__
        os.remove(file_address)

if __name__ == "__main__": 
    unittest.main()