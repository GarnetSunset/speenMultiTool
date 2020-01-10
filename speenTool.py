import os

# Get prereqs
from importlib import util
spam_loader = util.find_spec('playsound')
if (spam_loader is None):
    os.system("python -m pip install playsound")
    
import datetime, playsound, random, sys, time

cwd = os.getcwd()
now = datetime.datetime.now()
hour = now.strftime("%I")

if len(sys.argv) == 1:
    playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))
    exit()

if sys.argv[1] == "g":
    if int(hour) > 12:
        hour = hour - 12
    currentHour = int(hour)
    goUp = 0
    while goUp != currentHour:
        goUp += 1
        playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))

