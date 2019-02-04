from chain import blocks, nodes

block1 = blocks.block(1, 'test')
block2 = blocks.block(2, 'test2', block1.retrieve_hash())

for block in [block1, block2]:
    print(block.block_content())


