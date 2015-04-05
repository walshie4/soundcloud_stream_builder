#!/usr/bin/env python

import soundcloud

class soundcloud_stream_builder(object):

    def __init__(self, username, access_token=None):
        if access_token is None:
            self.sc = soundcloud.Client(client_id="265aecdf421a49f07a6c7f36a049f1b6")
            url = 'https://soundcloud.com/' + username
            self.my_id = self.sc.get('/resolve', url=url).id
        else:
            self.sc = soundcloud.Client(access_token=access_token)
            self.my_id = self.sc.get('/me').id

    def get_all_following(self):
        pass

    def get_most_recent_tracks(self, artist_id):
        pass

if __name__=="__main__":
    username = raw_input("username: ")
    stream = soundcloud_stream_builder(username)

