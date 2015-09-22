import subprocess, sys
from pydub import AudioSegment
from pydub.playback import play

def get_format(path=False, file=False):
    if path != False:
        if sys.platform == "linux":
            path_split = path.split('/')
        elif sys.platform == "win32":
            path_split = path.split('\\')
        tmp = path_split[len(path_split) - 1]
    elif file != False:
        tmp = file
    tmp1 = tmp.split('.')
    format = tmp1[len(tmp) - 1]
    return format

def play_file(path):
    format = get_format()
    if format == "mp3":
        song_process = AudioSegment.from_mp3(path)
    elif format == "ogg":
        song_process = AudioSegment.from_ogg(path)
    elif format == "flv":
        song_process = AudioSegment.from_flv(path)
    elif format == "wav":
        song_process = AudioSegment.from_wav(path)
    else:
        try:
            song_process = AudioSegment.from_file(path)
        except:
            return False
    play(song_process)

