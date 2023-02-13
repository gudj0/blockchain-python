from blockchain import Blockchain
from block import Block 
import uuid 

BLOCK_SIZE = 25 

if __name__=="__main__":

    # init blockchain and genesis block 
    bc = Blockchain() 
    g = Block(BLOCK_SIZE) 
    
    # init addresses 
    bob = uuid.uuid4().hex
    alice = uuid.uuid4().hex 
    trudy = uuid.uuid4().hex 

    # populate addresses with some cash through faucet
    bc.faucet(bob)
    bc.faucet(alice)

    # check initial balances
    print("Bob's balance: ", bc.get_balance(bob))
    print("Alice's balance: ", bc.get_balance(alice))

    # do some transactions
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(alice, bob)
    
    # add the genesis block 
    bc.add_block(g) 

    # add 100 empty blocks 
    for i in range(100):
        bc.add_block(Block(BLOCK_SIZE))

    # add some populated blocks 
    for i in range(50):
        new = Block(BLOCK_SIZE)
        new.tx(bob, trudy)
        bc.add_block(new)

    # check updated state (balances)
    print("Bob's balance: ", bc.get_balance(bob))
    print("Alice's balance: ", bc.get_balance(alice))
    print("Trudy's balance: ", bc.get_balance(trudy))

    # fetch some blocks from chain
    genesis = bc.get_block(1)
    hundreth = bc.get_block(100)
