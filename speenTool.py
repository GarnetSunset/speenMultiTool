import ctypes, datetime, os, playsound, pylnk, random, shutil, sys, time
from elevate import elevate

cwd = os.getcwd()
now = datetime.datetime.now()
hour = now.strftime("%I")

# Python 3 pylnk required: https://github.com/strayge/pylnk

if len(sys.argv) == 1:
    playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))
    exit()

try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

# g for grandfather clock mode
if sys.argv[1] == "-g":
    if int(hour) > 12:
        hour = hour - 12
    currentHour = int(hour)
    goUp = 0
    while goUp != currentHour:
        goUp += 1
        playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))

# install as a hotkey
if sys.argv[1] == "-i":
    if os.name == "nt":
        #whereisw = os.popen("where epythonw").read()
        link = pylnk.for_file(cwd+"\\speenTool.py")
        link.hot_key = "SHIFT+ALT+S"
        if is_admin == False:
            elevate()
        link.save("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\speen.lnk")
        print("Congrats! You should have speen now, usable by typing \"Shift + Alt + S\" whenever you want!\nYou will have to either reboot or log out and back in for it to begin working though.")
    else:
        print("No linux support yet")
        
if sys.argv[1] == "-u":
    if os.name == "nt":
        os.remove("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\speen.lnk")
        print("Removed!")
    else:
        print("No linux support yet.")
        
if sys.argv[1] == "-h":
    print("Running without an argument will give you a random speen.\nRunning with the argument \"g\" will run in grandfather clock mode (stroke for hours.)\nRunning with the argument \"i\" will install a speen hotkey that can be called with \"Shift + Alt + S.\"\nRunning with the argument \"u\" will uninstall the speen hotkey.\nRunning with the argument \"h\" will... seriously mate I think you know.")
