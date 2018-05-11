import configparser
from . import core_utils

config=configparser.ConfigParser()
try:
  configData = config.read('config.ini')
except FileNotFoundError:
  create=core_utils.createConfig()
  configData = config.read('config.ini') if create else print("Failed to create config.ini which is essential to the operations of the server.\nPlease confirm write permissions are granted and try again.") and exit(1)

@staticmethod
async def getConfigValue(section:str, field:str):
  return config[section.upper()][field.lower()]

@staticmethod
async def setConfigValue(section:str, field:str, value):
  return config.set(section, field, value)
