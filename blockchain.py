from collections import defaultdict

NUM_ACCOUNTS = 2 

# global variables used to track tx and block numbers
block_number = 0
tx_number = 0 

# the Transaction class represents a single Transaction in a Block
class Transaction():
    def __init__(self, sender, receiver):
        global tx_number
        self.sender = sender
        self.receiver = receiver 
        self.id = tx_number
        tx_number += 1 

# the Block class represents a Block in the Blockchain
class Block():
    
    # constructor
    def __init__(self, size):
        global block_number 
        self.prev = block_number 
        block_number += 1 
        self.num = block_number
        self.size = size
        self.transactions = []
        self.contents = hash(self)

    # performs a transaction given that it's within the size of the Block
    def tx(self, sender, receiver):       
        if len(self.transactions) >= self.size: 
            return False
        t = Transaction(sender, receiver) 
        self.transactions.append(t)
        return True

# the Blockchain class holds the chain itself and a ledger of address balances. 
class Blockchain():
    
    #constructor
    def __init__(self):
        self.chain = [] 
        self.state = defaultdict(int)
        self.current_block = 0
    
    # gets the balance of an address
    def get_balance(self, addr): 
        return self.state[addr]
    
    # adds a new block to the Blockchain
    def add_block(self, b):
        if not self.validate_block(b):
            return False 
        self.update_state(b)
        self.chain.append(b)
        self.current_block = b.num
        return True
        
    # gets a Block from the Blockchain given the block number 'num'  
    def get_block(self, num):
        for b in self.chain: 
            if b.num == num:
                return b
    
    # validates that a Block meets the criteria to be part of the chain
    def validate_block(self, b):
        if not b: 
            return False 
        
        if not isinstance(b, Block): 
            return False 
        
        if b.prev != self.current_block: 
            return False 

        if b.num <= self.current_block: 
            return False 
        return True

    # updates the Blockchain's ledger of address balances given a list of transactions from an incoming Block
    def update_state(self, b):
        for tx in b.transactions: 
            if self.state[tx.sender] == 0: 
                print("[transaction #%s]: failed due to low balance"%(tx.id))
                return
            self.state[tx.sender] -= 1    
            self.state[tx.receiver] += 1 
            print("[transaction #%s]: success [%s -> %s]"%(tx.id, tx.sender, tx.receiver))

    # (helper function) gives an address some balance 
    def faucet(self, addr): 
        self.state[addr] += 100
    