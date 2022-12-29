from backend.ecosystem.blockchain.consensus import Collector

class BlockChain:
    def __init__(self, id, collector: Collector):
        self.id = id
        self.collector = collector


class BlockImmutableError(Exception):
    def __init__(self, block):
        super().__init__('Block already has data. Block data is immutable. Create a new Block.'
                         f'\nexisting data: {block.data}')