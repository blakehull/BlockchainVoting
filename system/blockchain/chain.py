from system.blockchain.data import Block, BlockMetadata
from system.helpers.functions import generate_nonce
import json


class Chain:
    def __init__(self, genesis_hash=None):
        self.genesis_metadata = BlockMetadata(
            nonce=generate_nonce(),
            genesis_hash=genesis_hash,
            previous_hash="genesis",
            version=1.0
        )
        self.genesis_block = Block({}, self.genesis_metadata)
        self.blocks = [self.genesis_block]

    def __str__(self):
        loaded = [json.loads(x.__str__()) for x in self.blocks]
        return json.dumps(loaded, indent=4)

    def add_block(self, block: Block):
        prev_block = self.blocks[-1]
        block.create_metadata(prev_block)
        self.blocks.append(block)
