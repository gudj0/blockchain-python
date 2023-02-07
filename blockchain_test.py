from blockchain import Block, Blockchain 
import uuid 

BLOCK_SIZE = 25 

# tests the functionality of the Blockchain.validate_block() function
def test_validate_block(bc, alice, bob):
     
    # should not allow a lower or equal block number to the last block
    b = Block(BLOCK_SIZE)
    b.num = bc.current_block - 1
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    res = bc.add_block(b)
    assert res == False, "Should not allow a lower or equal block number to the last block"

    # block without a valid previous block should not be added
    b = Block(BLOCK_SIZE)
    b.num = bc.current_block + 2
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    res = bc.add_block(b)
    assert res == False, "Block with a >1 higher block number should not be added"

    # should not allow null type to be added as Block
    b = None
    res = bc.add_block(b)
    assert res == False, "Should not allow null type to be added as Block"


    # should not allow invalid object type to be added as Block
    b = Blockchain()
    res = bc.add_block(b)
    assert res == False, "Should not allow Blockchain type to be added as Block"

     # tx from empty balance should fail
    b = Block(BLOCK_SIZE) 
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    bc.add_block(b)
    assert bc.get_balance(alice) == alice_init, "Tx from sender with zero-balance should not change chain's state"


# tests the functionality of the Blockchain.update_state() function
def test_update_state(bc, bob, alice):
    # populate addresses with some cash through faucet
    bc.faucet(bob)
    bc.faucet(alice)


    # tx from empty balance should fail
    b = Block(BLOCK_SIZE) 
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    bc.add_block(b)
    assert bc.get_balance(alice) == alice_init, "Tx from sender with zero-balance should not change chain's state"


    # blockchain state should initialize any new address to 0
    b = Block(BLOCK_SIZE) 
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(alice, new_address) 
    bc.add_block(b)
    assert bc.state[new_address] != None , "Blockchain state should initialize any new address to 0"



if __name__=="__main__":

    # init blockchain and genesis block 
    bc = Blockchain() 
    g = Block(BLOCK_SIZE) 
    
    # init addresses 
    bob = uuid.uuid4().hex
    alice = uuid.uuid4().hex 
    
    # test functions
    test_update_state(bc, bob, alice) 
    test_validate_block(bc, bob, alice) 

