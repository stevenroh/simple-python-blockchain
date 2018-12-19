import os
from block import Block
import datetime as date
from genesis import create_genesis_block

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

running = True

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

def display_blockchain():
    for b in blockchain:
        print(b)

def add_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = data
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Ask the user to input data and add blocks to the chain
while running:
    data = input("\nInsert some data for the new block : ")

    if data == "":
        running = False
    else:
        block_to_add = add_block(previous_block, data)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        cls()
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        # print("Hash: {}\n".format(block_to_add.hash))

    display_blockchain()