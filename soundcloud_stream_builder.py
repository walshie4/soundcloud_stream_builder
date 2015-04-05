#!/usr/bin/env python

import soundcloud

class soundcloud_stream_builder(object):

    def __init__(self, id_value):
        self.soundcloud.Client(id_value)

    def get_all_following(self):
        pass

    def get_most_recent_tracks(self, artist_id):
        pass

if __init__=="__main__":
    client_id = int(raw_input("id: "))
    stream = soundcloud_stream_builder(client_id)

