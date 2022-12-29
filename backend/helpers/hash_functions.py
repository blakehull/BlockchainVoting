import hashlib


class Functions:
    def hash_it(self, tohash):
        return hashlib.sha512(tohash.encode('utf-8')).hexdigest()
