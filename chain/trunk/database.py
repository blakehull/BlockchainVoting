import redis
import json


class Database:
    def __init__(self,pw=None):
        self.r = redis.Redis(host='localhost', port=6379, password=pw)

    def instance(self):
        return self.r

    def peek(self):
        for x in self.r.keys():
            if x.decode().contains("block"):
                print(x.decode(), self.r.get(x).decode())

    def save_blocks(self, blocks, blockhash):
        content = {}
        for x in blocks[1:]:
            x = json.loads(x)
            content['vote'] = x['content']['vote']
            content['hash'] = x['hash']
            content['block'] = x
        self.r.set("block:" + blockhash, str(content))

    def get(self, key):
        return json.loads(self.r.get(key).decode().replace("\'", "\""))

    def get_all_blocks(self):
        to_return = []
        for x in self.r.keys():
            if "block" in x.decode():
                print(self.r.get(x).decode().replace("\'", "\""))
                to_return.append(self.r.get(x).decode().replace("\'", "\""))
        return to_return
