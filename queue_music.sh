#!/bin/bash
# dependencies
#   - mpd
#   - mpc
#   - youtube-dl
#   - python3 
#       - googlesearch
# optional 
#   -ncmpcpp 
if [ -f "links.tmp" ]
then
    rm -f links.tmp
fi
/usr/bin/python3 get_music.py
for link in `cat links.tmp | grep -v playlist | grep -v channel`
do
    mpc add `youtube-dl -g --quiet $link`
done
mpc shuffle
