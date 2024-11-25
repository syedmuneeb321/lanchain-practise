import logging




def get_logger(name):

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a console handler to print to the screen
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)


    # Create a file handler to save logs to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


