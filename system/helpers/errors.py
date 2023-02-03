class BlockImmutableError(Exception):
    def __init__(self, block):
        super().__init__('Block already has data. Block data is immutable. Create a new Block.'
                         f'\nexisting data: {block.data}')

class BlockMetadataExists(Exception):
    def __init__(self, block):
        super().__init__('Block already has metadata. Block data is immutable. Create a new Block.'
                         f'\nexisting data: {block.metadata}')