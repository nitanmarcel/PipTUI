import configparser
from pathlib import Path
import os

HOME_DIR = str(Path.home())
PIPTUI_DIR = HOME_DIR + '/.piptui/'
CONFIG_PATH = PIPTUI_DIR + 'config.ini'
THEME_FOLDER = PIPTUI_DIR + 'themes/'

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def get_config_value(option, as_bool=False):
    if as_bool is True:
        return config.getboolean('DEFAULT', option)
    else:
        return config.get('DEFAULT', option)


def set_config_value(option, value):
    with open(CONFIG_PATH, 'w') as configfile:
        config.set('DEFAULT', option, value)
        config.write(configfile)
