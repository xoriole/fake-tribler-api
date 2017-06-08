import json
from twisted.web import resource


class WalletsEndpoint(resource.Resource):

    def render_GET(self, request):
        wallets = {"DUM1": {
            "created": True,
            "name": "DUM1",
            "address": "DUMMYADDRESS1",
            "balance": {
                "available": 50,
                "pending": 0.0,
            }}, "DUM2": {
            "created": True,
            "name": "DUM2",
            "address": "DUMMYADDRESS2",
            "balance": {
                "available": 90,
                "pending": 0.0,
            }}}
        return json.dumps({"wallets": wallets})
