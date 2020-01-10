import datetime, os, playsound, random, shutil, sys, time

cwd = os.getcwd()
now = datetime.datetime.now()
hour = now.strftime("%I")

if len(sys.argv) == 1:
    playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))
    exit()

# g for grandfather clock mode
if sys.argv[1] == "g":
    if int(hour) > 12:
        hour = hour - 12
    currentHour = int(hour)
    goUp = 0
    while goUp != currentHour:
        goUp += 1
        playsound.playsound(cwd + "\speens\\" + random.choice(os.listdir(cwd+"\speens\\")))

if sys.argv[1] == "i":
    print("h")
