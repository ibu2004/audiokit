# Gets root privileges
echo Requires your password to install dependencies.
sudo su

# Installs dependencies
apt-get install -y libavbin0 libav-tools python3-tk
pip3 install pyglet

# Installs program.
mv raspbian-music /usr/local/bin
#mv raspbian-music.desktop /usr/share/applications

# Prints confirmation
echo
echo Successfully installed raspbian music!
echo No desktop shortcut yet. Sorry! Execute by typing raspbian-music...
