# Music-streamer
simple script to stream my favourite artists from youtube --no-audio --no-browser --no-player

Python script to fetch music videos from my favourite aritists and play them in background.
Its a wrapper around youtube-dl and googlesearch python library. 

  - Reads configurations from conf.json and does a boolean search to generate links. 
  - Youtube-dl converts them to a link which can be streamed.
  - mpc queue the links to mpd playlist 

## Requirements 
Any linux machine . 

## Dependencies 

  - mpd (music player daemon)  & mpc 
    ```sudo apt install mpd mpc -y```
  - [youtube-dl](https://github.com/ytdl-org/youtube-dl)
    ```
    sudo apt install curl -y
    sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl
    ``` 
  - python
    - [googlesearch](https://python-googlesearch.readthedocs.io/en/latest/)
    ```pip install google```
  - ncmpcpp(optional) : n curses musicplayer client ++
    
# Usage 
  - clone the repository 
  - edit conf.json to add your favourite artists
  - change permissions of scripts ```chmod 755 que_music.sh get_music.py```
  - run the bash script ```./queu_music```
 Note that the scripts just queue the links - play with your favourite client - say ncmpcpp or just open another terminal after a few seconds and type ```mpc toggle```
 
 ### caveats
 adding mashups in conf file may result in songs of various artists



