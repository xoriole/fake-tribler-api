import random

import time


class Tick:

    def __init__(self, price_type, quantity_type, is_ask=True):
        self.is_ask = is_ask
        self.trader_id = ''.join(random.choice('0123456789abcdef') for n in xrange(16))
        self.timeout = 3600
        self.price_type = price_type
        self.quantity_type = quantity_type

        now = int(time.time())
        self.timestamp = random.randint(now - 3600, now)
        self.price = random.randint(1, 100)
        self.quantity = random.randint(1, 100)
        self.order_number = random.randint(1, 50)
        self.message_id = ''.join(random.choice('0123456789abcdef') for n in xrange(16))

    def get_json(self):
        return {
            "trader_id": self.trader_id,
            "timeout": self.timeout,
            "quantity_type": self.quantity_type,
            "price_type": self.price_type,
            "timestamp": self.timestamp,
            "price": self.price,
            "order_number": self.order_number,
            "message_id": self.message_id,
            "quantity": self.quantity
        }
