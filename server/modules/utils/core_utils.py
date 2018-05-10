import configparser, uuid, os
from argon2 import PasswordHasher
from . import settings

async def credCheck(credentials):
  PasswordHasher

def createConfig():
  config=configparser.ConfigParser()
  config['DEFAULT']={'Name':'Librarium','FileCompression':'true','CompressionLevel':'9'}
  config['SERVER']={'Domain':'127.0.0.1'}
  config['DATABASE']={'Name':'Librarium','Address':'127.0.0.1','Port':'27017','Username':'','Password':''}
  config['SECURITY']={'EncryptionType':'SHA-1','Salt':generateSalt()}
  with open('config.ini', 'w') as configfile: config.write(configfile)
  
async def createStorageDir(dirName):
  baseStorageDirName=str('/'+os.path.relpath('../..','/')).replace('\\','/')+f'/{settings.getConfigValue("default","name")}/'
  if not os.path.isdir(baseStorageDirName):
    os.mkdir(baseStorageDirName)
  if dirName is list:
    dirName='/'.join(dirName)
  os.mkdir(str(baseStorageDirName+dirName).replace('//','/'))