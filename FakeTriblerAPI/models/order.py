import random

import time


class Order:

    def __init__(self, price_type, quantity_type):
        self.trader_id = ''.join(random.choice('0123456789abcdef') for n in xrange(16))
        now = int(time.time())
        self.timestamp = random.randint(now - 3600, now)
        self.price_type = price_type
        self.quantity_type = quantity_type
        self.price = random.randint(1, 100)
        self.quantity = random.randint(1, 100)
        self.reserved_quantity = random.randint(0, self.quantity)
        self.traded_quantity = random.randint(0, self.quantity)
        self.is_ask = random.random() < 0.5
        self.order_number = random.randint(1, 50)
        self.status = random.choice(['open', 'completed', 'expired', 'cancelled'])

    def get_json(self):
        return {
            "trader_id": self.trader_id,
            "timestamp": self.timestamp,
            "price": self.price,
            "quantity_type": self.quantity_type,
            "reserved_quantity": self.reserved_quantity,
            "is_ask": self.is_ask,
            "price_type": self.price_type,
            "timeout": 3600,
            "traded_quantity": self.traded_quantity,
            "order_number": self.order_number,
            "completed_timestamp": None,
            "quantity": self.quantity,
            "status": self.status
        }
