import time
import hashlib
import json

class block:
  def __init__(self, index, data, previousHash):
    self.block = {
      'index': index,
      'timestamp': time.time(),
      'data': data,
      'previousHash': previousHash,
      'nonce': 0,
    }

  def hashBlock(self):
    """Returns the hash for a block"""
    hasher = hashlib.sha256
    block = str(self.block).encode('utf-8')
    return hasher(block).hexdigest()
  
  def validProof(self):
    """Checks if the nonce for the Proof of work (POW) algorithm is correct"""
    difficulty = 3
    hash = self.hashBlock()
    hash = hash[:difficulty]
    return hash == '000'

  def findProof(self):
    """Finds the correct nonce for the POW"""
    nonce = self.block['nonce']
    while self.validProof() is False:
      self.block['nonce'] += 1

    return self

class blockchain:
  def __init__(self):
    self.chain = []
    self.genesisBlock()

  def genesisBlock(self):
    """Create the first block with special input"""
    genBlock = block(0, "Gensis Block", 0).findProof()
    self.chain.append(genBlock)

  def mine(self):
    """Find and add a new block on the chain"""
    newblock = block(len(self.chain), {}, self.chain[-1].hashBlock())
    newblock.findProof()
    self.chain.append(newblock)

  
# print(newblock.findProof())
# print(newblock.block['nonce'], newblock.hashBlock())

def main():
  bitcoin = blockchain()

  for i in range():
    bitcoin.mine()

  print(len(bitcoin.chain))
  for block in bitcoin.chain:
    print(json.dumps(block.block, indent=2))


if __name__ == '__main__':
  main()