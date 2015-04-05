#!/usr/bin/env python

import soundcloud
from datetime import datetime

class soundcloud_stream_builder(object):

    def __init__(self, username, access_token=None):
        if access_token is None:
            self.sc = soundcloud.Client(client_id="265aecdf421a49f07a6c7f36a049f1b6")
            url = 'https://soundcloud.com/' + username
            self.my_id = self.sc.get('/resolve', url=url).id
        else:
            self.sc = soundcloud.Client(access_token=access_token)
            self.my_id = self.sc.get('/me').id
        for artist in self.get_all_following():
            self.get_most_recent_tracks(artist.id)

    def get_all_following(self):
        return self.sc.get('/users/' + str(self.my_id) + '/followings')

    def get_most_recent_tracks(self, artist_id):
        tracks = self.sc.get('/users/' + str(artist_id) + '/tracks')
        for track in tracks:
            time = datetime.strptime(track.created_at[:-6], "%Y/%m/%d %H:%M:%S")
            print time

if __name__=="__main__":
    username = raw_input("username: ")
    stream = soundcloud_stream_builder(username)

