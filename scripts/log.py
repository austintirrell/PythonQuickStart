import os
import logging


# Collects all `logger.error()` calls
# Import and use `ERROR_COLLECTOR` if needed
ERROR_COLLECTOR = []


class CustomLogger(logging.Logger):
    def error(self, msg, *args, **kwargs):
        ERROR_COLLECTOR.append(msg)
        super().error(msg, *args, **kwargs)


logging.setLoggerClass(CustomLogger)
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def setup_logger(name, log_file, level=logging.INFO):
    FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    HANDLER = logging.FileHandler(log_file)        
    HANDLER.setFormatter(FORMATTER)
    LOGGER = logging.getLogger(name)
    LOGGER.setLevel(level)
    LOGGER.addHandler(HANDLER)
    return LOGGER


# Set up loggers here...
MAIN_LOG = setup_logger('main_logger', os.path.join('logs', 'main.log'))
TEST_LOG = setup_logger('test_logger', os.path.join('logs', 'test.log'))

HELPER_LOG = setup_logger('helper_logger', os.path.join('logs', 'helper.log'))