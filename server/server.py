from flask import Flask
from modules.utils import settings, core_utils
import asyncio

app = Flask(settings.getConfigValue('default', 'name'))

# todo actually work on the REST interface
@app.route('/')
def hello_world():
  return 'Hello World!'

async def init():
  app.run(debug=True)

if __name__ == '__main__':
  loop=asyncio.get_event_loop()
  loop.run_until_complete(init())
