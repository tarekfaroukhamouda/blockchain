# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from hashlib import sha256


from block import  Block
from blockchain import Blockchain

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=0
    blockchain=Blockchain()
    database=['Hello','AShmrd','Youssid']
    for d in database:
         num+=1
         blockchain.mine(Block(d,num))
    print(blockchain.chain)
    print(blockchain.isVaild())



