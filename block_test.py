from block import Block
from blockchain import Blockchain

import uuid 

BLOCK_SIZE = 25 

# tests the functionality of the tx function in Block
def test_tx(bc, bob, alice):

    # populate addresses with some cash through faucet
    bc.faucet(bob)
    bc.faucet(alice)

    # senders and receivers balance should decrease and increase, respectively
    b = Block(BLOCK_SIZE) 
    bob_init = bc.get_balance(bob)
    alice_init = bc.get_balance(alice)
    b.tx(bob, alice) 
    bc.add_block(b)
    assert bc.get_balance(bob) == bob_init-1, "Senders balance should decrease"
    assert bc.get_balance(alice) == alice_init+1, "Receivers balance should increase"

    # should allow sending to a completely new address
    b = Block(BLOCK_SIZE) 
    new_address = uuid.uuid4().hex
    b.tx(bob, new_address) 
    bc.add_block(b)
    assert bc.get_balance(new_address) == 1, "Balance should be 1 when receiving first tx on fresh address"

    # block should not allow more than 25 tx'
    b = Block(BLOCK_SIZE) 
    bc.faucet(bob)

    for i in range(100):
        res = b.tx(bob, alice)
        if i > BLOCK_SIZE:
            assert res == False, "Should not allow >25 txs per block"
            break

if __name__=="__main__":

    # init blockchain and genesis block 
    bc = Blockchain() 
    
    # init addresses 
    bob = uuid.uuid4().hex
    alice = uuid.uuid4().hex 
    
    # test transactions
    test_tx(bc, bob, alice) 
 