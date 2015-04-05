#!/usr/bin/env python

import soundcloud

class soundcloud_stream_builder(object):

    def __init__(self, user_id, access_token = None):
        if access_token is None:
            self.sc = soundcloud.Client("265aecdf421a49f07a6c7f36a049f1b6")
        else:
            self.sc = soundcloud.Client(access_token=access_token)

    def get_all_following(self):
        pass

    def get_most_recent_tracks(self, artist_id):
        pass

if __init__=="__main__":
    user_id = int(raw_input("user id: "))
    stream = soundcloud_stream_builder(user_id)

