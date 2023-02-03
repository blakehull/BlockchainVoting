from system.helpers.functions import hash_it, generate_nonce
from datetime import datetime
import json


class BlockMetadata:
    def __init__(self, nonce, genesis_hash, previous_hash, version=1.0):
        self.version = version
        self.nonce = nonce
        self.genesis_hash = genesis_hash
        self.previous_hash = previous_hash
        self.hashed_metadata = hash_it(
            [version, nonce, previous_hash]
        )

    def __str__(self):
        return json.dumps({
            "version": self.version,
            "genesis_hash": self.genesis_hash,
            "previous_hash": self.previous_hash,
            "hash": self.hashed_metadata
        })


class Block:

    def __init__(self, data: dict, metadata: BlockMetadata = None):
        self.data = data
        self.timestamp = datetime.utcnow().isoformat()
        self.nonce = generate_nonce()
        self.metadata = metadata
        if metadata is not None:
            self.metadata = metadata

    def __str__(self):
        if self.metadata is None:
            safe_metadata = self.metadata
        else:
            safe_metadata = json.loads(self.metadata.__str__())
        return json.dumps({
            "data": self.data,
            "timestamp": self.timestamp,
            "metadata": safe_metadata
        })

    def create_metadata(self, block):
        if self.metadata is None:
            self.metadata = BlockMetadata(
                nonce=generate_nonce(),
                genesis_hash=block.metadata.genesis_hash,
                previous_hash=block.metadata.hashed_metadata
            )
            return True
