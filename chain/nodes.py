import json
from chain.trunk import database

class Node:
    def __init__(self, blocks):
        self.r = database.Database(pw="yumyum")
        self.blocks = blocks
        self.blockhash = self.blocks.chain_hash()

    def __save__(self):
        self.r.save_blocks(self.blocks.get_blocks(), self.blockhash)
        return 'saved'

    def verify(self):
        prev_hash = None
        ind = 0
        for x in self.blocks.get_blocks():
            if json.loads(x)['prevhash'] != prev_hash:
                raise Exception("possible insertion at index: " + str(ind) + "\n -- previous hash: " + prev_hash + "\n -- block content: " + "\n" + json.dumps(json.JSONDecoder().decode(x)))
            ind += 1
            prev_hash = json.loads(x)['hash']
        return self.__save__()

    def block(self):
        return self.blocks

    def database(self):
        return self.r
