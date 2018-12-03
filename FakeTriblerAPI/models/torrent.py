from random import randint, uniform
import time


class Torrent:

    def __init__(self, infohash, name, length, category):
        self.infohash = infohash
        self.name = name
        self.length = length
        self.category = category
        self.files = []
        self.time_added = randint(1200000000, 1460000000)
        self.relevance_score = uniform(0, 20)

        self.num_seeders = randint(0, 500) if randint(0, 1) == 0 else 0
        self.num_leechers = randint(0, 500) if randint(0, 1) == 0 else 0

    def get_json(self):
        return {
            "name": self.name,
            "infohash": self.infohash.encode('hex'),
            "size": self.length,
            "category": self.category,
            "relevance_score": self.relevance_score,
            "num_seeders": self.num_seeders,
            "num_leechers": self.num_leechers,
            "last_tracker_check": time.time()
        }
