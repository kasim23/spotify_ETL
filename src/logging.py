import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger"""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example of using the logger
logger = setup_logger('spotify_etl_logger', 'spotify_etl.log')