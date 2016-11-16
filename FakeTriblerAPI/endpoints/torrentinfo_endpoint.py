import json
from twisted.web import resource


class TorrentInfoEndpoint(resource.Resource):

    def render_GET(self, request):
        metainfo_dict = {"metainfo": {"info": {"files": [{"path": "/test1/file1.txt", "length": 1234},
                                                         {"path": "/test1/file2.txt", "length": 2534}]}}}
        return json.dumps(metainfo_dict)
