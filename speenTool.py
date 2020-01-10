import os

# Get prereqs
from importlib import util
spam_loader = util.find_spec('playsound')
if (spam_loader is None):
    os.system("python -m pip install playsound")
spam_loader = util.find_spec('win32con')
if (spam_loader is None):
    os.system("python -m pip install pypiwin32")
    print("Run this program again if it errors out with \"win32com\" it's just a flaw of python")
spam_loader = util.find_spec('winshell')
if (spam_loader is None):
    os.system("python -m pip install winshell")

import playsound, random, time, winshell

cwd = os.getcwd()
playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))
