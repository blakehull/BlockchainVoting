import sqlite3
from sqlite3 import Error

class Node:
    def __init__(self,nodename = None):
        self.nodename = nodename
        self.compile = {}
        create_connection("chain/chainbase/nodedb.db")

    def save(self, data):
        self.compile[data[0]] = data[1]
        return 'saved'

    def verify(self, hash):
        return self.compile[hash]


class Masternode(Node):
    def __init__(self):
        self.nodes = []

    def update_nodes(self, node_id):
        self.nodes.append([node_id])

    def network_nodes(self):
        return self.nodes

