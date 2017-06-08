import random

import time


class Transaction:

    def __init__(self, price_type, quantity_type):
        self.trader_id = ''.join(random.choice('0123456789abcdef') for _ in xrange(16))
        self.partner_trader_id = ''.join(random.choice('0123456789abcdef') for _ in xrange(16))
        self.order_number = random.randint(1, 50)
        self.partner_order_number = random.randint(1, 50)
        self.transaction_number = random.randint(1, 50)
        self.price = random.randint(1, 100)
        self.price_type = price_type
        self.transferred_price = random.randint(0, self.price)
        self.quantity = random.randint(1, 100)
        self.quantity_type = quantity_type
        self.transferred_quantity = random.randint(0, self.quantity)
        now = int(time.time())
        self.timestamp = random.randint(now - 3600, now)
        self.payment_complete = random.random() > 0.5
        self.status = random.choice(['pending', 'completed', 'error'])

    def get_json(self):
        return {
            "trader_id": self.trader_id,
            "order_number": self.order_number,
            "partner_trader_id": self.partner_trader_id,
            "partner_order_number": self.partner_order_number,
            "transaction_number": self.transaction_number,
            "price": self.price,
            "price_type": self.price_type,
            "transferred_price": self.transferred_price,
            "quantity": self.quantity,
            "quantity_type": self.quantity_type,
            "transferred_quantity": self.transferred_quantity,
            "timestamp": self.timestamp,
            "payment_complete": self.payment_complete,
            "status": self.status
        }
