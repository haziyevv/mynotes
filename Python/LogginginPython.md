**Logging Library**

1) There are six logging levels in Python. 

2) Highest level is **CRITICAL**. If you set your logging level to **CRITICAL**, only messages of the **CRITICAL** level will be shown.

To set logging level to **CRITICAL**

```
logging.basicConfig(level=logging.CRITICAL)
```

or

```
logging.basicConfig(level=50)
```

3) Logging levels from lowest to highest are: **NOTSET=0**, **DEBUG**=10, **INFO=20**, **WARNING=30**, **ERROR=40**, **CRITICAL=50**.
4. The default level of logging is **WARNING**. Which means, the logging module will only display warnings, errors and critical severity.

5. You can format the logging messages to log in the given format you want. For example you can add the date and time to the log messages:

```
logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', 
                    level= logging.NOTSET)


logging.debug("Here you have some information for debugging.")
logging.info("Everything is normal. Relax!")


--> this will output:

2021-02-14 23:02:34,089 | DEBUG: Here you have some information for debugging.
2021-02-14 23:02:34,089 | INFO: Everything is normal. Relax!

```

Available attributes to use: **[url](https://docs.python.org/3/library/logging.html#logrecord-attributes)**

6. If you want to write the log to a file instead, just add ass atribute to the **logging.basicConfig**

```
logging.basicConfig(filename='sample.log', format='%(asctime)s | %(levelname)s:',
                    level=logging.NotSet)
```



# More advance logging

To use more advanced logging use logger object.

Steps --> 

1) create logger object 

2) set the lowest security level 

3) set a desitination also called a handler. This could be **StreamHandler** to write to console or **FileHandler** to write to a file. 

4) set format of messages for the handler.

```
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler()

log_format = "%(asctime)s | %(levelname)s: %(message)s"
console_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(console_handler)
```



## Loguru

1. to load :

   ```python
   from loguru import logger
   ```

2. File logging with rotation / retention / compression

   ```python
   logger.add("logger_file.log") --> will configure output log file to given file
   logger.add("log_file.log", rotation="5 KB") --> if the size of the file passes 5kb start from clean
   logger.add("out.log", backtrace=True, diagnose=True)  --> will show the full backtrace info
   ```

3. How to use logger in order to catch any exception from a function ?

   ```python
   @logger.catch
   def my_function(x, y, z):
   	return 1/(x+y+z)
   ```

4. If you want async logging:

   ```python
   logger.add("somefile.log", enqueue=True)
   ```

5. 

