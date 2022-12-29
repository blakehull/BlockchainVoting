from backend.ecosystem.blockchain.block import Block
from backend.ecosystem.blockchain.supers import BlockChain


class Chain(BlockChain):
    def __init__(self, blockchain_id):
        super().__init__(blockchain_id)
        self.genesis_block = Block("special_hash")
        self.blocks = [self.genesis_block]

    def add_block(self, block):
        if self.validate_block(block):
            self.blocks.append(block)
            return True
        else:
            return False

    def validate_block(self, block):
        return block.data is not None and block.metadata.genesis_hash == self.genesis_block.genesis_hash