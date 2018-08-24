import json
from twisted.web import resource

from FakeTriblerAPI import tribler_utils


class IPv8Endpoint(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild("trustchain", IPv8TrustChainEndpoint())


class IPv8TrustChainEndpoint(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild("users", IPv8TrustChainUsersEndpoint())


class IPv8TrustChainUsersEndpoint(resource.Resource):

    def getChild(self, path, request):
        return IPv8TrustChainSpecificUserEndpoint(path)


class IPv8TrustChainSpecificUserEndpoint(resource.Resource):

    def __init__(self, _):
        resource.Resource.__init__(self)
        self.putChild("blocks", IPv8TrustChainSpecificUserBlocksEndpoint())


class IPv8TrustChainSpecificUserBlocksEndpoint(resource.Resource):

    def render_GET(self, request):
        return json.dumps({"blocks": [block.to_dictionary() for block in tribler_utils.tribler_data.trustchain_blocks]})
