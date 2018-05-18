from flask import Flask, abort, make_response, jsonify
from modules import file_management as fmanage
import asyncio, aiohttp
import os
from modules.utils import settings

app = Flask(settings.Config.getConfigValue('default', 'name'))

# todo actually work on the REST interface
@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/api/v1.0/account/create', methods=['POST'])
def gen_account(*args, **kwargs):
  return security.account.generate()

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({"error": "Not found"}), 404)

@app.route('/api/v1.0/file/upload', methods=['POST'])
async def uploadToServer(fileUrl:str, payload):
  return await fmanage.download(fileUrl, payload, loop=aiohttp.ClientSession(loop=loop))

async def init():
  app.run(debug=True)

if __name__ == '__main__':
  import platform
  if platform.system().lower() == 'windows':
    l = []
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      if os.path.isdir(f'{letter}:\\'):
        l.append(letter)
    for letter in l:
      try:
        dir = f'{letter}:\\'+os.path.relpath('.',f'{letter}:\\')
        break
      except ValueError:
        pass
    del l
    baseDir = dir
  else:
    baseDir = '/'+os.path.relpath('.', '/')
  print(baseDir)
  
  loop = asyncio.get_event_loop()
  loop.run_until_complete(init())
