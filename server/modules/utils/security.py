# general pypi packages
import os, platform, secrets, uuid

# server-specific packages
from . import settings
from .. import file_management

try:
  import argon2
except ImportError:
  print('Run "pip install argon2_cffi" to continue.')

class type(object):
  """Types used for SecurityBase.generateSecret(type:int)"""
  def __init__(self):
    self.user=type._user()
    self.session=type._session()
    self.connection=type._initialConnection()
  
  @staticmethod
  def _user():
    return 0
  
  @staticmethod
  def _session():
    return 1
  
  @staticmethod
  def _initialConnection():
    return 2
  
class account(object):
  
  async def generate(self, name:str, email:str, gpg_pubkey, *args, **kwargs):
    pass
  
class SecurityBase:

  async def generateSecret(self, type:int):
    """Types are in the type(object) class.
      If you're changing this, leave the length at 32 so you don't break anything."""
    if type == 0: # user
      return secrets.token_bytes(32) # used as the salt for argon2id password + oauth2 encrypting
    elif type == 1: # session
      return secrets.token_hex(32) # used to encrypt the streams for ReST
    elif type == 2: # connection
      return secrets.token_urlsafe(32) # used to identify which connection is which while streaming (downloading/uploading)
    else:
      raise NotImplementedError # in case you fuckers change any code here.

class GPG:
  
  @staticmethod
  def checkGPGExists():
    """Name self-explanatory."""
    return file_management.executableIsExecutable('gpg')
  
