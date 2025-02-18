<h1>Logging Framework</h1>
<h3>Requirements</h3>

<ul><li>Should be able to log different categories of logs such as DEBUG, INFO, WARNING, ERROR, CRITICAL</li>
<li>Multiple outputs should be able to write logs in various destinations like console, file, database</li>
<li>Should provide flexibility to add/remove default logging levels and destinations</li>
</ul>




basic design points to consider:
- Since we have different log levels we can have an enum class to define the log level 
- we should have different message output handlers such as stream handlers (console logging), file handler (log file).
- will use chain of responsibility design pattern since we have different log levels which also has hierarchy
- So we should have a Log manager to create the chain of responsibility for the different logger 
- we will have an abstract logger handler and the child classes will be the info logger, debug logger, warning logger, error logger, critical logger etc
- we will use observer design pattern to sync the message for the logs



```mermaid
classDiagram

class LogLevel{
    <<enumeration>>
        CRITICAL
        ERROR
        WARNING
        INFO
        DEBUG
}

class AbstractLogger{
    <<abstract>>
    - my_log_level: LogLevel
    + setNextLogger(next_level_logger: AbstractLogger)
    + logMessage(log_level: LogLevel, log_message: string, logger_subject: LoggerSubject)

    + routeMessage(message: string, logger_subject: LoggerSubject)
    + get_log_level(): LogLevel
}
class DebugLogger {
    + next_level_logger: AbstractLogger
    
    + routeMessage(message: string, logger_subject: LoggerSubject)
} 

class InfoLogger {
    + next_level_logger: AbstractLogger
    
    + routeMessage(message: string, logger_subject: LoggerSubject)
} 

class WarningLogger {
    + next_level_logger: AbstractLogger
    
    + routeMessage(message: string, logger_subject: LoggerSubject)
} 

class ErrorLogger {
    + next_level_logger: AbstractLogger
    
    + routeMessage(message: string, logger_subject: LoggerSubject)
} 

class CriticalLogger {
    + next_level_logger: AbstractLogger
    
    + routeMessage(message: string, logger_subject: LoggerSubject)
} 
AbstractLogger ..> LogLevel: Dependency
AbstractLogger <|-- DebugLogger: Extends
AbstractLogger <|-- InfoLogger: Extends
AbstractLogger <|-- WarningLogger: Extends
AbstractLogger <|-- ErrorLogger: Extends
AbstractLogger <|-- CriticalLogger: Extends
```