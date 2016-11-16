from random import randint, uniform
import binascii
import time


class Torrent:

    def __init__(self, id, infohash, name, length, category):
        self.id = id
        self.infohash = binascii.a2b_base64(infohash).encode('hex')
        self.name = name
        self.length = int(length)
        self.category = category
        self.files = []
        self.time_added = randint(1200000000, 1460000000)
        self.relevance_score = uniform(0, 20)

        self.num_seeders = randint(0, 500) if randint(0, 1) == 0 else 0
        self.num_leechers = randint(0, 500) if randint(0, 1) == 0 else 0

    def get_json(self):
        return {"name": self.name, "infohash": self.infohash, "size": self.length, "category": self.category,
                "relevance_score": self.relevance_score, "num_seeders": self.num_seeders,
                "num_leechers": self.num_leechers, "last_tracker_check": time.time()}
