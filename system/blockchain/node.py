from system.helpers.functions import generate_nonce


class Node:
    def __init__(self, address, secret):
        self.address = address
        self.secret = secret
        self.id = generate_nonce()
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend.id)