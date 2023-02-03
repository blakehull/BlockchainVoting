from system.blockchain.chain import Chain
from system.blockchain.data import Block

chain = Chain("tonight")
block = Block({'hi': True})
block2 = Block({'hi': False})
print(block)
chain.add_block(block)
chain.add_block(block2)
print(chain)

