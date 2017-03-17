import base64
import json
from random import randint

from twisted.web import resource

from FakeTriblerAPI import tribler_utils


class MultichainEndpoint(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)

        child_handler_dict = {"statistics": MultichainStatsEndpoint, "blocks": MultichainBlocksEndpoint}

        for path, child_cls in child_handler_dict.iteritems():
            self.putChild(path, child_cls())


class MultichainStatsEndpoint(resource.Resource):
    """
    This class handles requests regarding the multichain community information.
    """

    def render_GET(self, request):
        last_block = tribler_utils.tribler_data.multichain_blocks[-1]

        return json.dumps({'statistics': {
            "id": ('a' * 20).encode("hex"),
            "total_blocks": len(tribler_utils.tribler_data.multichain_blocks),
            "total_down": last_block.total_down,
            "total_up": last_block.total_up,
            "peers_that_pk_helped": randint(10, 50),
            "peers_that_helped_pk": randint(10, 50),
            "latest_block": last_block.to_dictionary()
        }})

class MultichainBlocksEndpoint(resource.Resource):
    """
    This class handles requests regarding the multichain community blocks.
    """

    def getChild(self, path, request):
        return MultichainBlocksIdentityEndpoint(path)


class MultichainBlocksIdentityEndpoint(resource.Resource):
    """
    This class represents requests for blocks of a specific identity.
    """

    def __init__(self, identity):
        resource.Resource.__init__(self)
        self.identity = identity

    def render_GET(self, request):
        """
        Return some random blocks
        """
        return json.dumps({"blocks": [block.to_dictionary() for block in tribler_utils.tribler_data.multichain_blocks]})
