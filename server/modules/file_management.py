# general pypi packages
import os
import posixpath
import aiohttp, async_timeout
from urllib.parse import urlsplit, unquote
from shutil import which

# server-specific packages

def filename(url):
  urlPath = urlsplit(url).path
  basename = posixpath.basename(unquote(urlPath))
  if os.path.basename(basename) != basename or unquote(posixpath.basename(urlPath)) != basename:
    raise ValueError # rejects duplicate name on windows (fuck windows compatibility requirements)
  return basename

async def download(url, payload, loop): # todo make oauth2 integration a thing
  with async_timeout.timeout(10):
    fname = filename(url)
    async with aiohttp.ClientSession(loop=loop).get(url) as response:
      with open(fname, 'wb') as f:
        while True:
          chunk = await response.content.read()
          if not chunk:
            break
          f.write(chunk)
      return await response.release()

def executableIsExecutable(fname:str):
  """Name is self-explanatory
  return payload is:
    [a, b] a = whether or not exe exists and is in path, b = path if it exists and is in path"""
  w = which(fname).replace('\\','\\')
  if w == None:
    return False
  return [True, w] # return is [executableExists:bool, path:str]
    