import logging

logging.basicConfig(
    filename='../LOGS/simple.log',  # defaults to STDERR
    level=logging.WARNING,  # defaults to WARNING
)

logging.warning('This is a warning') # message will be output
logging.debug('This message is for debugging') # message will NOT be output
logging.error('This is an ERROR') # message will be output
logging.critical('This is ***CRITICAL***') # message will be output
logging.info('The capital of North Dakota is Bismark') # message will not be output

