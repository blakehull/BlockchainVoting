import datetime
from backend.ecosystem.blockchain.chain import Chain
from backend.ecosystem.blockchain.supers import BlockImmutableError
from backend.helpers.hash_functions import Functions


class BlockMetadata:
    def __init__(self, version, timestamp, nonce, genesis_hash, previous_hash):
        self.version = version
        self.timestamp = timestamp
        self.nonce = nonce
        self.genesis_hash = genesis_hash
        self.previous_hash = previous_hash
        self.authenticated = False
        self.user = None
        self.hashed_metadata = Functions.hash_it([version, timestamp, nonce, genesis_hash, previous_hash])


class Block:

    def __init__(self):
        self.data = None
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.nonce = self.timestamp
        self.genesis_hash = None
        self.metadata = BlockMetadata()

    def add_data(self, json):
        if self.data is None:
            self.data = json
            return True
        else:
            raise BlockImmutableError(self)