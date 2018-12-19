import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str("%s%s%s%s" % (self.index, self.timestamp, self.data, self.previous_hash)).encode("utf-8"))
        return sha.hexdigest()

    def __str__(self):
        return str("Block #%s : [HASH = %s] [DATA = %s] [PREVIOUS = %s]" % (self.index, self.hash, self.data, self.previous_hash))