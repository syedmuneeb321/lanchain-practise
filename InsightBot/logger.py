import logging 
import os 


os.makedirs("logs",exist_ok=True)

def get_logger(name: str):
    """
        Configures and returns a logger instance.

    """

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    return logging.getLogger(name)


