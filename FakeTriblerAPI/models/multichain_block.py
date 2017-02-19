import base64
from random import randint, random

import datetime


class MultichainBlock:

    def __init__(self, my_id=None, timestamp=0, seq_num=0, last_block=None):
        self.up = randint(1, 10000)
        self.down = randint(1, 10000)
        self.is_requester = False
        self.tot_up_prev_block = 0
        self.tot_down_prev_block = 0

        if last_block:
            if last_block.is_requester:
                self.tot_up_prev_block = last_block.total_up_requester + last_block.up
                self.tot_down_prev_block = last_block.total_down_requester + last_block.down
            else:
                self.tot_up_prev_block = last_block.total_up_responder + last_block.down
                self.tot_down_prev_block = last_block.total_down_responder + last_block.up

        if random() > 0.5:
            # We are the requester of the block
            self.is_requester = True
            if last_block is None:
                self.sequence_number_requester = 0
            else:
                self.sequence_number_requester = seq_num

            self.total_up_requester = self.tot_up_prev_block
            self.total_down_requester = self.tot_down_prev_block
            self.total_up_responder = randint(0, 100000)
            self.total_down_responder = randint(0, 100000)
            self.sequence_number_responder = randint(1, 1000)
            self.public_key_requester = my_id
            self.public_key_responder = 'b' * 20
        else:
            # We are the responder of the block
            if last_block is None:
                self.sequence_number_responder = 0
            else:
                self.sequence_number_responder = seq_num

            self.total_up_responder = self.tot_up_prev_block
            self.total_down_responder = self.tot_down_prev_block
            self.total_up_requester = randint(0, 100000)
            self.total_down_requester = randint(0, 100000)
            self.sequence_number_requester = randint(1, 1000)
            self.public_key_requester = 'b' * 20
            self.public_key_responder = my_id

        self.previous_hash_requester = 'a' * 20
        self.previous_hash_responder = 'b' * 20
        self.signature_requester = 'c' * 20
        self.signature_responder = 'd' * 20

        self.insert_time = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    def to_dictionary(self):
        return {
            "up": self.up,
            "down": self.down,
            "total_up_requester": self.total_up_requester,
            "total_down_requester": self.total_down_requester,
            "sequence_number_requester": self.sequence_number_requester,
            "previous_hash_requester": base64.encodestring(self.previous_hash_requester).strip(),
            "total_up_responder": self.total_up_responder,
            "total_down_responder": self.total_down_responder,
            "sequence_number_responder": self.sequence_number_responder,
            "previous_hash_responder": base64.encodestring(self.previous_hash_responder).strip(),
            "public_key_requester": base64.encodestring(self.public_key_requester).strip(),
            "signature_requester": base64.encodestring(self.signature_requester).strip(),
            "public_key_responder": base64.encodestring(self.public_key_responder).strip(),
            "signature_responder": base64.encodestring(self.signature_responder).strip(),
            "insert_time": self.insert_time
        }
