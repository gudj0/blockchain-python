from collections import defaultdict

NUM_ACCOUNTS = 2 
block_number = 0
tx_number = 0 

class Transaction():
    def __init__(self, sender, receiver):
        global tx_number
        self.sender = sender
        self.receiver = receiver 
        self.id = tx_number
        tx_number += 1 


class Block():
    def __init__(self, size):
        global block_number 
        self.prev = block_number 
        block_number += 1 
        self.num = block_number
        self.size = size
        self.transactions = []
        self.contents = hash(self)

    def tx(self, sender, receiver):       
        if len(self.transactions) >= self.size: 
            return False
        t = Transaction(sender, receiver) 
        self.transactions.append(t)
        return True


class Blockchain():
    def __init__(self):
        self.chain = [] 
        self.state = defaultdict(int)
        self.current_block = 0

    def get_balance(self, addr): 
        return self.state[addr]
    
    def add_block(self, b):
        self.validate_block(b)
        self.update_state(b)
        self.chain.append(b)
        self.current_block = b.num
    
    def get_block(self, num):
        for b in self.chain: 
            if b.num == num:
                return b

    def validate_block(self, b):
        if b.num <= self.current_block: 
            raise Exception("block number is invalid")
        if not isinstance(b, Block): 
            raise TypeError("block type is invalid")
        

    def update_state(self, b):
        for tx in b.transactions: 
            if self.state[tx.sender] == 0: 
                print("[transaction #%s]: failed due to low balance"%(tx.id))
                return
            self.state[tx.sender] -= 1    
            self.state[tx.receiver] += 1 
            print("[transaction #%s]: success [%s -> %s]"%(tx.id, tx.sender, tx.receiver))

    # gives an address some balance 
    def faucet(self, addr): 
        self.state[addr] += 100
    