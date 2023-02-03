import hashlib
from random import Random
import sys


def hash_it(tohash):
    return hashlib.sha512(str(tohash).encode()).hexdigest()


def generate_nonce():
    return Random().randint(1, sys.maxsize)
