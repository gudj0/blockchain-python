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