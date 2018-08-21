import json
from random import randint, choice

from twisted.web import resource


class StatisticsEndpoint(resource.Resource):
    """
    This endpoint is responsible for handing requests regarding statistics in Tribler.
    """

    def __init__(self):
        resource.Resource.__init__(self)

        child_handler_dict = {"tribler": StatisticsTriblerEndpoint, "ipv8": StatisticsIPv8Endpoint,
                              "communities": StatisticsCommunitiesEndpoint}

        for path, child_cls in child_handler_dict.iteritems():
            self.putChild(path, child_cls())


class StatisticsTriblerEndpoint(resource.Resource):
    """
    This class handles requests regarding Tribler statistics.
    """
    def render_GET(self, request):
        return json.dumps({'tribler_statistics': {
            "num_channels": randint(5, 100),
            "database_size": randint(1000, 1000000),
            "torrents": {
                "num_collected": randint(5, 100),
                "total_size": randint(1000, 100000),
                "num_files": randint(5, 100)
            }
        }})


class StatisticsIPv8Endpoint(resource.Resource):
    """
    This class handles requests regarding IPv8 statistics.
    """
    def render_GET(self, request):
        return json.dumps({'ipv8_statistics': {
            "total_up": 13423,
            "total_down": 3252
        }})


class StatisticsCommunitiesEndpoint(resource.Resource):
    """
    This class handles requests regarding IPv8 communities statistics.
    """
    def render_GET(self, request):
        return json.dumps({'ipv8_overlay_statistics': [{
            "master_peer": ''.join(choice('0123456789abcdef') for _ in xrange(20)),
            "my_peer": ''.join(choice('0123456789abcdef') for _ in xrange(20)),
            "global_time": randint(1, 10000),
            "peers": [],
            "overlay_name": "TestOverlay"
        }]})
