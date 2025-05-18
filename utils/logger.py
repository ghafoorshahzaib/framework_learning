import logging
import os


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        # File handler with directory creation
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
                logger.info(f"Created logs directory: {log_dir}")
            except PermissionError as e:
                logger.error(f"Failed to create logs directory: {e}")
                return logger
        try:
            fh = logging.FileHandler(os.path.join(log_dir, 'test.log'))
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.info("File handler added successfully")
        except Exception as e:
            logger.error(f"Failed to add file handler: {e}")
    return logger
