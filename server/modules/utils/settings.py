import configparser
from . import core_utils

cfgparse=configparser.ConfigParser(inline_comment_prefixes=('|'))
try:
  configData = cfgparse.read('config.ini')
except FileNotFoundError:
  create = core_utils.createConfig()
  configData = cfgparse.read('config.ini') if create else print("Failed to create config.ini which is essential to the operations of the server.\nPlease confirm write permissions are granted and try again.") and exit(1)

class Config:
  
  def getConfigValue(self, section:str, option:str):
    section = section.upper(); option = option.lower()
    try:
      get = cfgparse.getboolean(section, option)
    except ValueError:
      try:
        get = cfgparse.getfloat(section, option)
      except ValueError:
        get = cfgparse.get(section, option)
    return get

async def setConfigValue(section:str, option:str, value):
  return config.set(section, option, value)

@staticmethod
def name():
  return cfgparse.get('SERVER', 'name')

class Server:
  
  @classmethod
  def domain(cls):
    return cfgparse.get('SERVER', 'domain')
  
  @classmethod
  def defaultDirectory(cls):
    return cfgparse.get('SERVER', 'defaultdirectory')
  
  @classmethod
  def fileCompression(cls):
    return cfgparse.getboolean('SERVER', 'filecompression')
  
  @classmethod
  def fileCompressionLevel(cls):
    return cfgparse.getint('SERVER', 'compressionlevel')

class Database:
  
  @classmethod
  def address(cls):
    return [cfgparse.get('DATABASE', 'address'), cfgparse.getint('DATABASE', 'port')]
  
  @classmethod
  def credentials(cls):
    return [cfgparse.get('DATABASE', 'username'), cfgparse.get('DATABASE', 'password')]
  
    