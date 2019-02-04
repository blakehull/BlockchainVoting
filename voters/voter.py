from voters.security import RSA
import hashlib

keygen = RSA

class voter:
    def __init__(self):
        return None

    def register(self):
        id = input("enter id: ")
        tohash = str(keygen.find_primes()) + id
        return hashlib.sha512(tohash).hexdigest()

    def verify_registration(self, id = None):
        return None