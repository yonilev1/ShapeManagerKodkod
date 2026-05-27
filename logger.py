import logging


def get_logger(name):
        """
        gets name and returns configed logger 

        Args:
            name(str): name of logger

        Returns:
            logging: the configed logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(f"{name}_logs.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s, %(name)s, %(levelname)s, %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger