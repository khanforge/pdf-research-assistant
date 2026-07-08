from utils.logger import setup_logger

logger = setup_logger("test_logger")

logger.info("This is an info message from test_logger.")
logger.warning("This is an warning message from test_logger.")
logger.error("This is an error message from test_logger.")