import json

from twisted.web import resource

from FakeTriblerAPI import tribler_utils


class MarketEndpoint(resource.Resource):
    """
    This class represents the root endpoint of the market community API where we trade reputation.
    """

    def __init__(self):
        resource.Resource.__init__(self)

        child_handler_dict = {"asks": AsksEndpoint, "bids": BidsEndpoint,
                              "transactions": TransactionsEndpoint, "orders": OrdersEndpoint}
        for path, child_cls in child_handler_dict.iteritems():
            self.putChild(path, child_cls())


class AsksEndpoint(resource.Resource):

    def render_GET(self, request):
        return json.dumps({
            "asks": [{
                "price_type": "DUM1",
                "quantity_type": "DUM2",
                "ticks": [tick.get_json() for tick in tribler_utils.tribler_data.order_book['asks']]
            }]
        })


class BidsEndpoint(resource.Resource):

    def render_GET(self, request):
        return json.dumps({
            "bids": [{
                "price_type": "DUM1",
                "quantity_type": "DUM2",
                "ticks": [tick.get_json() for tick in tribler_utils.tribler_data.order_book['bids']]
            }]
        })


class TransactionsEndpoint(resource.Resource):

    def render_GET(self, request):
        return json.dumps({"transactions": [transaction.get_json() for
                                            transaction in tribler_utils.tribler_data.transactions]})


class OrdersEndpoint(resource.Resource):

    def render_GET(self, request):
        return json.dumps({"orders": [order.get_json() for order in tribler_utils.tribler_data.orders]})
