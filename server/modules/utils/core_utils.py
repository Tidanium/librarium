import configparser, uuid
import os, platform
import argon2, secrets
import server
from . import settings

def createConfig():
  config=configparser.ConfigParser()
  config['DEFAULT']={'Name':'Librarium','FileCompression':'true','CompressionLevel':'9'}
  config['SERVER']={'Domain':'127.0.0.1'}
  config['DATABASE']={'Name':'Librarium','Address':'127.0.0.1','Port':'27017','Username':'','Password':''}
  with open('config.ini', 'w') as configfile: config.write(configfile)
  
async def createStorageDir(dirName):
  baseStorageDirName=str('/'+os.path.relpath('../..','/')).replace('\\','/')+f'/{settings.getConfigValue("default","name")}/'
  if not os.path.isdir(baseStorageDirName):
    os.mkdir(baseStorageDirName)
  if dirName is list:
    dirName='/'.join(dirName)
  os.mkdir(str(baseStorageDirName+dirName).replace('//','/')) # just in case

class security:
  def __init__(self):
    self.secretType={"user":0, "session":0,"connection":1}
  
  async def credCheck(self, cred:dict):
    cred['user'] # todo motor check for user to grab user dictionary and work off that
  
  async def credCreate(self, cred:dict):
    
    pass # todo motor check if username or email exists already. different action based on which
  
  async def generateSecret(self, t:int):
    if t == 0:
      return secrets.token_bytes(32)
    elif t == 1:
      return secrets.token_hex(32)
    else:
      raise NotImplementedError

class GPG:
  def __init__(self):
    def gpgExe():
      if platform.system().lower() == 'windows':
        if not 'gnupg-w32cli-{settings.getConfigValue("windows","gpgversion")}.exe' in os.listdir(f'{server.baseDir}/bin/'):
          import urllib
          urllib.urlretrieve(f'ftp://ftp.gnupg.org/gcrypt/binary/gnupg-w32cli-{settings.getConfigValue("windows","gpgversion")}.exe')
          os.system()
