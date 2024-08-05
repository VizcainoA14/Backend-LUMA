import os
from configparser import ConfigParser

CONFIG = ".config"


def set_up():
    """Sets up configuration for the app"""

    env = os.getenv("ENV", CONFIG)

    if env == CONFIG:
        config = ConfigParser()
        config.read(CONFIG)
        config = config["DATA"]

    return config
