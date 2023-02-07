from blockchain import Block, Blockchain
import uuid 
BLOCK_SIZE = 25 

if __name__=="__main__":

    # init blockchain and genesis block 
    bc = Blockchain() 
    g = Block(BLOCK_SIZE) 
    
    # init addresses 
    bob = uuid.uuid4().hex
    alice = uuid.uuid4().hex 
    
    # populate addresses with some cash through faucet
    bc.faucet(bob)
    bc.faucet(alice)

    # check initial balances
    print(bc.get_balance(bob))
    print(bc.get_balance(alice))

    # do some transactions
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(bob, alice)
    g.tx(alice, bob)
    g.tx(alice, bob)
    g.tx(alice, bob)
    g.tx(alice, bob)
    g.tx(alice, bob)
    
    # add the genesis block 
    bc.add_block(g) 

    # check updated state (balances)
    print(bc.get_balance(bob))
    print(bc.get_balance(alice))

    # fetch the genesis block from chain
    genesis_block = bc.get_block(1)
    print(genesis_block)