import os, re

# Get prereqs
from importlib import util
spam_loader = util.find_spec('playsound')
if (spam_loader is None):
    os.system("python -m pip install playsound")
spam_loader = util.find_spec('win32con')
if (spam_loader is None):
    os.system("python -m pip install pypiwin32")
spam_loader = util.find_spec('winshell')
if (spam_loader is None):
    os.system("python -m pip install winshell")

import playsound, time, winshell

cwd = os.getcwd()
playsound.playsound(cwd+"\speens\speen.mp3")