#!/usr/bin/env python

import soundcloud
from datetime import datetime
import time

class soundcloud_stream_builder(object):

    def __init__(self, username, access_token=None):
        if access_token is None:
            self.sc = soundcloud.Client(client_id="265aecdf421a49f07a6c7f36a049f1b6")
            url = 'https://soundcloud.com/' + username
            self.my_id = self.sc.get('/resolve', url=url).id
        else:
            self.sc = soundcloud.Client(access_token=access_token)
            self.my_id = self.sc.get('/me').id
        recent = list()
        print("gathering the users you follow...")
        for artist in self.get_all_following():
            print "Getting tracks for artist - " + artist['username']
            recent.extend(self.get_most_recent_tracks(artist['id']))
        recent.sort(key=lambda track: self.sc_timestamp_to_datetime(track.created_at))
        for track in recent:
            print track.title

    def get_all_following(self, offset=0, limit=100):
        resp = self.sc.get('/users/' + str(self.my_id) + '/followings',
                linked_partitioning=1, limit=limit, offset=offset * limit)
        result = []
        try:
            next_href = resp.next_href
            print(next_href)
            offset += 1
            print('getting page #' + str(offset))
            for each in resp.collection:
                result.append(each)
            result += self.get_all_following(offset=offset)
        except AttributeError:
            pass
        for res in resp.collection:
            result.append(res)
        print(len(result))
        return result

    # Defaults to those within the past 30 days
    def get_most_recent_tracks(self, artist_id, age_to_disqualify=2592000):
        tracks = self.sc.get('/users/' + str(artist_id) + '/tracks')
        with_stream = list()
        for track in tracks:
            try:
                test = track.stream_url
                with_stream.append(track)
            except AttributeError:
                continue
        recent = list()
        for track in tracks:
            time = self.sc_timestamp_to_datetime(track.created_at)
            age = (datetime.now() - time).total_seconds()
            if age < age_to_disqualify:#include
                recent.append(track)
        return recent

    def sc_timestamp_to_datetime(self, timestamp):
        return datetime.strptime(timestamp[:-6], "%Y/%m/%d %H:%M:%S")

if __name__=="__main__":
    username = raw_input("username: ")
    start = time.time()
    print "building stream for " + username + "..."
    stream = soundcloud_stream_builder(username)
    print "stream built in " + str(time.time() - start) + " seconds"

