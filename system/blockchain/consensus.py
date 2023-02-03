from system.blockchain.chain import Chain


class Negotiator:
    def __init__(self):
        self.nodes = {}

    def register_node(self, node):
        if node.id not in self.nodes:
            self.nodes[node.id] = {
                "address": node.address,
                "secret": node.secret,
                "friends": node.friends
            }
