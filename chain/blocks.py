import datetime
import hashlib

class block:
    def __init__(self, index, content, prevhash = None):
        self.time = datetime.datetime.utcnow().isoformat()
        self.index = index
        self.content = content
        self.prevhash = prevhash
        tohash = str(self.time) + str(self.index) + str(self.content) + str(self.prevhash)
        self.hash = hashlib.sha512(tohash.encode('utf-8')).hexdigest()
        self.log = [self.hash, self.index, self.content, self.time, self.prevhash]

    def retrieve_hash(self):
        return self.hash

    def block_content(self):
        return self.log

    def get_index(self):
        return self.id

    def previous_hash_index(self):
        return self.prevhash