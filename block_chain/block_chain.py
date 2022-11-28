from hashlib import sha256
from datetime import datetime


# A block of blockchain contains the following
# 1. Index
# 2. Timestamp
# 3. Data
# 4. Hash of the previous block
# 5. Hash of the current block]

# function to hash a block

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = sha256()
        sha.update(str(self.index).encode('utf-8') 
        + str(self.timestamp).encode('utf-8') 
        + str(self.data).encode('utf-8') 
        + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return f"<Block: {self.index}, {self.timestamp}, {self.data}, {self.previous_hash}, {self.hash}>"

class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, datetime.now(), "Genesis Block", "0"))

    def get_previous_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_previous_block().hash
        new_block.hash = new_block.hash_block()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.hash_block():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        for block in self.chain:
            print(block)


def main():
    blockchain = BlockChain()
    for i in range(4):
        # 1) block data: 
        data = input(f"{i+1}) block data: ")
        blockchain.add_block(Block(i+1, datetime.now(), data, blockchain.get_previous_block().hash))


    blockchain.print_chain()
    print(f"Is blockchain valid? {blockchain.is_valid()}")


if __name__ == "__main__":
    main()