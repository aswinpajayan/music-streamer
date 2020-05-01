#!/bin/bash
# dependencies
#   - mpd
#   - mpc
#   - youtube-dl
#   - python3 
#       - googlesearch
# optional 
#   -ncmpcpp 
/usr/bin/python3 get_music.py
for link in `cat links.tmp`
do
    mpc add `youtube-dl -g --quiet link`
done
