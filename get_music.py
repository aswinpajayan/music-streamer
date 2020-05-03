'''get the youtube links for music videos'''

import json
import random

class MusicBrowser:
    ''' Class to get links for youtube videos
    args : artist name'''
    def __init__(self, artist, params):
        self.num = params['num_of_tracks']
        self.query = "site:" + params['site']
        self.query += " (intitle:" + " OR ".join(params['intitle']) + ")"
        self.query += " \"" + artist['name'] + "\" -channel"
        self.query += " -playlist -cover"
        if 'tags' in artist:
            self.query += " " + " ".join(artist['tags'])
        self.tracks = ""
        print(self.query)
    def get_tracks(self):
        ''' method to generate links for youtube videos '''
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' Found, check venv")
        self.tracks = search(query=self.query,
                             lang='en', num=self.num, stop=self.num, pause=20)

    def get_playlists(self, get_list=False):
        ''' is_list = True returns playlist url'''
        if get_list:
            self.query = self.query + " AND playlist"
        else:
            self.query = self.query + " -playlist"


def main():
    '''main method'''
    playlist = []
    with open("conf.json", "r") as global_conf:
        conf = (json.load(global_conf))
    for artist in conf['artists']:
        print(artist['name'])
        browser = MusicBrowser(artist, params=conf['global_params'])
        browser.get_tracks()
        for track in browser.tracks:
            playlist.append(track)
    random.shuffle(playlist)
    print(playlist)
    playlist = "\n".join(playlist)
    with open("links.tmp", "w") as link_file:
        link_file.write(playlist)


if __name__ == '__main__':
    main()
