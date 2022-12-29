from backend.ecosystem.blockchain.chain import Chain


class Negotiator:
    def __init__(self, chain: Chain, protocols = None):
        self.working_chain = chain

    def add_block(self, block):
        self.working_chain.add_block(block)
        return
