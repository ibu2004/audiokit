import subprocess

def omxplayer_control(file, args, ignite=True):
    global omxplayer
    if ignite == True:
        omxplayer = subprocess.Popen(["omxplayer", args, file], universal_newlines=True)
    elif ignite == False:
        omxplayer.kill()


def omxplayer_communication(command="play"):
    if command == "play" or command == "pause":
        omxplayer.communicate("p")
    elif command == "stop":
        omxplayer.kill()