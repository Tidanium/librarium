import secrets

try:
  import argon2
except ImportError:
  print('Run "pip install argon2_cffi" to continue.')

class type(object):
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
  
  async def generate(self, name, email, gpg_pubkey, *args, **kwargs):
  
  