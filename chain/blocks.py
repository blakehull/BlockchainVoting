import datetime
import hashlib
import json
from collections import Counter


def __content__(content):
    return {'id': content[0],
            'vote': content[1]}


def hash_it(tohash):
    return hashlib.sha512(tohash.encode('utf-8')).hexdigest()


class BlockModule:
    def __init__(self):
        self.current_index = 0
        self.blocks = [self.__genesis_block__()]

    def __genesis_block__(self):
        time = datetime.datetime.utcnow().isoformat()
        hash = str(time) + str(self.current_index) + str(['genesis', '']) + str(None)
        return json.dumps({"index": self.current_index,
                           "content": __content__(['genesis', '']),
                           "hash": hash_it(hash),
                           "time": time,
                           "prevhash": None})

    def create_block(self, content):
        self.current_index += 1
        time = datetime.datetime.utcnow().isoformat()
        prevhash = self.get_block_hash(self.current_index - 1)
        hash = str(time) + str(self.current_index) + str(content) + str(prevhash)
        return json.dumps({"index": self.current_index,
                           "content": __content__(content),
                           "hash": hash_it(hash),
                           "time": time,
                           "prevhash": prevhash})

    def add_block(self, block):
        self.blocks.append(block)
        return None

    def get_block_hash(self, index):
        return json.loads(self.blocks[index])['hash']

    def view_chain(self):
        for x in self.blocks:
            print(json.dumps(json.JSONDecoder().decode(x)))
        return None

    def get_blocks(self):
        return self.blocks

    def winner(self, blocks=None):
        if blocks is None:
            blocks = self.blocks[1:]
        votes = []
        for x in blocks:
            votes.append(json.loads(x)['vote'])
        return Counter(votes).most_common(1)

    def chain_hash(self):
        return hash_it(str(self.blocks))
