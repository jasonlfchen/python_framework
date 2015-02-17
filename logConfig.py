# sample of how to configure & create the logger

__auther__ = 'Sam Albin'
import logging
import logging.config

# get logger configration
logging.config.fileConfig('logging.ini')
# create logger
logger = logging.getLogger('fileLog')

# sample loggers
logger.info('info test message')
logger.warn('warn test message')
logger.error('error test message')
logger.critical('critical test message')
