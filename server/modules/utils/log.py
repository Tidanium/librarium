import os
import server

path = server.baseDir+'temp'
if not os.path.isdir(path):
  os.mkdir(path)
fileList = [path+f'log-server', path+'argon2',]
def checkLogExists(file:str=None):
  if file:
    fileList.append(path+'/'+file)
  for f in fileList:
    if os.path.isfile(f):
      pass
