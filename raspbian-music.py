# Raspbian Music, a music player for Linux-based ARM devices (mainly RPi)
# Copyright (C) 2015 Ibrahim Ansari

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Importing modules
import pyglet
from tkinter import *

# Initialize player
player = pyglet.media.Player()

# Tkinter GUI
class Player():
    def __init__(self):
        global player
        player = pyglet.media.Player()

    def queue_player(self, file):
        player.queue(file)

    def player_play(self):
        player.play()

    def player_pause(self):
        player.pause()

    def skip(self):
        player.next_source()

    def seek(self, time):
        player.seek(time)

#    def set_volume(self, volume=False):
#        if volume != False:
#            volume = float(volume)
#            player.volume(volume)
#        player.volume