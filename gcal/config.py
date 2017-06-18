"""
Read Config file and load values into namespace
"""
from ConfigParser import ConfigParser
import ipdb

CONFIG = ConfigParser()
CONFIG.read('settings.ini')

CLIENT_ID = CONFIG["CLIENT"]["CLIENT_ID"]
CLIENT_SECRET = CONFIG["CLIENT"]["CLIENT_SECRET"]

