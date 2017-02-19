import base64
import json

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
            "self_id": base64.encodestring('a' * 20).strip(),
            "latest_block_insert_time": "2016-08-04 12:01:53",
            "self_total_blocks": len(tribler_utils.tribler_data.multichain_blocks),
            "latest_block_id": "32428fdsjkl3f3",
            "latest_block_requester_id": "fdjklfdhfeek3",
            "latest_block_up_mb": 34,
            "self_total_down_mb": last_block.total_down_requester
            if last_block.is_requester else last_block.total_down_responder,
            "latest_block_down_mb": 85,
            "self_total_up_mb": last_block.total_up_requester
            if last_block.is_requester else last_block.total_up_responder,
            "latest_block_responder_id": "f83ldsmhqio"
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
