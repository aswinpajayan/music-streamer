#!/bin/bash
# dependencies
#   - mpd
#   - mpc
#   - youtube-dl
#   - python3 
#       - googlesearch
# optional 
#   -ncmpcpp 
link_fifo="links.fifo"
if [ -p "$link_fifo" ]
then
    echo "fifo exists"
else
    echo "creating ... fifo"
    mkfifo  "$link_fifo"
fi
/usr/bin/python3 get_music.py & 
echo ".................python in background......."

while true
do                # read line from link_fifo
    if read line; then
        if [ "$line" = 'quit' ]; then           # if line is quit, quit
            printf "%s: 'quit' command received\n" "$link_fifo"
            break
        fi
        echo "getting link....to queue"
        mpc add `youtube-dl -g --quiet $line`
    fi
done <"$link_fifo"

#for link in `cat links.tmp | grep -v playlist | grep -v channel`
#do
#    mpc add `youtube-dl -g --quiet $link`
#done
mpc shuffle
