import logging

logging.basicConfig (
    level = logging.DEBUG, 
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt = '%Y-%m-%d %H:%M:%S', 
    handlers = [
        logging.FileHandler('Lesson_002-Logging/log_file.log'), 
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('arithmentic_app')

def add(a, b) :
    result = a + b
    logger.info(f'Adding {a} + {b} = {result}')
    return result

def subtract(a, b) :
    result = a - b
    logger.info(f'Subtracting {a} - {b} = {result}')

def divide(a, b) :
    result = a / b
    logger.debug(f'dividing {a} / {b} = {result}')

def multiply(a, b) :
    result = a * b
    logger.info(f'Multiplying {a} * {b} = {result}')


add(10, 15)
subtract(10, 15)
divide(100, 10)
multiply(10, 15)