import datetime
import hashlib
import json

def hash_it(tohash):
    return hashlib.sha512(tohash.encode('utf-8')).hexdigest()

class Block:
    def __init__(self, content, previous_block):

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
