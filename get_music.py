#!/usr/bin/python3
import youtube_dl


class MusicBrowser:
    ''' Class to get links for youtube videos
    args : artist name'''
    def __init__(self, artist_name):
        self.artist = "site:youtube.com (intitle:hits OR song OR mashup)\"" + artist_name + "\" -channel"
        self.tracks = ""

    def get_tracks(self):
        ''' method to generate links for youtube videos '''
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' Found, check venv")
        self.tracks = search(query=self.artist,
                             lang='en', num=10, stop=5)

    def get_playlists(self, get_list=False):
        ''' is_list = True returns playlist url'''
        if get_list:
            self.artist = self.artist + " AND playlist"
        else:
            self.artist = self.artist + " -playlist"


def main():
    '''main method'''
    playlist = []
    sithara = MusicBrowser("Sithara Krishnakumar")
    sithara.get_tracks()
    for track in sithara.tracks:
        playlist.append(track)
    print(playlist)


if __name__ == '__main__':
    main()
