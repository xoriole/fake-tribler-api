from twisted.web import resource

from FakeTriblerAPI.endpoints.channels.channels_endpoint import ChannelsEndpoint
from FakeTriblerAPI.endpoints.downloads_endpoint import DownloadsEndpoint
from FakeTriblerAPI.endpoints.events_endpoint import EventsEndpoint
from FakeTriblerAPI.endpoints.multichain_endpoint import MultichainEndpoint
from FakeTriblerAPI.endpoints.mychannel_endpoint import MyChannelEndpoint
from FakeTriblerAPI.endpoints.search_endpoint import SearchEndpoint
from FakeTriblerAPI.endpoints.shutdown_endpoint import ShutdownEndpoint
from FakeTriblerAPI.endpoints.state_endpoint import StateEndpoint
from FakeTriblerAPI.endpoints.statistics_endpoint import StatisticsEndpoint
from FakeTriblerAPI.endpoints.torrentinfo_endpoint import TorrentInfoEndpoint
from FakeTriblerAPI.endpoints.torrents_endpoint import TorrentsEndpoint
from FakeTriblerAPI.endpoints.variables_endpoint import VariablesEndpoint
from FakeTriblerAPI.endpoints.settings_endpoint import SettingsEndpoint


class RootEndpoint(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)

        self.events_endpoint = EventsEndpoint()
        self.putChild("events", self.events_endpoint)

        self.search_endpoint = SearchEndpoint(self.events_endpoint)
        self.putChild("search", self.search_endpoint)

        child_handler_dict = {"channels": ChannelsEndpoint, "mychannel": MyChannelEndpoint,
                              "settings": SettingsEndpoint, "variables": VariablesEndpoint,
                              "downloads": DownloadsEndpoint, "torrents": TorrentsEndpoint,
                              "multichain": MultichainEndpoint, "statistics": StatisticsEndpoint,
                              "state": StateEndpoint, "torrentinfo": TorrentInfoEndpoint,
                              "shutdown": ShutdownEndpoint}

        for path, child_cls in child_handler_dict.iteritems():
            self.putChild(path, child_cls())
