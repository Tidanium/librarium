from . import settings
from motor.motor_asyncio import AsyncIOMotorClient

class motor:
  """These should be self-explanatory function names"""
  @staticmethod
  def credentials():
    l = []
    for i in ['username', 'password']:
      s = settings.Config.getConfigValue('database', i)
      if s == '':
        del l, i
        return False
      else:
        l.append(s)
    del i
    return {'username': l[0], 'password': l[1]}
  
  @staticmethod
  def address():
    return {'address':settings.Config.getConfigValue('database', 'address'), 'port':settings.Config.getConfigValue('database', 'port')}
  
  @staticmethod
  def name():
    return settings.Config.getConfigValue('database', 'name')
  
@staticmethod
def URI():
  """Returns the connection URI based on the config.ini file's contents"""
  mongoURI = ''
  if motor.credentials != False:
    fmt = f'{motor.credentials["username"]}:{motor.credentials["password"]}@'
    mongoURI += fmt
    del fmt
  if motor.address['port'] != 27017:
    fmt = ':'+motor.address['port']
  else:
    fmt = ''
  mongoURI += f'{motor.address["address"]}{fmt}'
  del fmt
  return mongoURI

@staticmethod
def client():
  """Static link to MongoDB connection."""
  return AsyncIOMotorClient(URI)


# todo get the rest of the work done for management of the database
