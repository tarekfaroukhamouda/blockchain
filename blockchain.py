from hashlib import  sha256

from block import Block

class Blockchain():
    difficulty=3

    def __init__(self,chain=[]):
        self.chain=chain

    def add(self,block):
        self.chain.append({"hash":block.set_hash(),
                           "previous":block.previous_hash,
                           "data":block.data,
                           "Nonce":block.nonce,
                           'number':block.number})
    def mine(self,block):
        try:
            block.previous_hash=self.chain[-1].get('hash')
        except IndexError:
            pass

        while True:
            print(block.set_hash())

            if block.set_hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                print(block)
                break
            else:
                block.nonce+=1
    def isVaild(self):
        for i in range(1,len(self.chain)):
            _previous=self.chain[i].get('previous')
            _current=self.chain[i-1].get('hash')
            if _previous !=_current or _current[:self.difficulty] != "0" * self.difficulty:
                return False
            return True