import json
from trunk import database


class Node:
    def __init__(self, address):
        self.pointer = address
        pass