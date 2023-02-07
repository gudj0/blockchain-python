from blockchain import Block, Blockchain 
import uuid 

BLOCK_SIZE = 25 

# tests the functionality of the Blockchain.validate_block() function
def test_validate_block(bc, alice, bob):
     
    # should not allow invalid type of object to be added as Block
    init_block = bc.current_block 
    b = Block(BLOCK_SIZE)
    b.num = 666
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    bc.add_block(b)
    assert bc.current_block == init_block, "Block without a valid previous block should not be added"


    "Should not allow invalid block object to be added"

     # tx from empty balance should fail
    b = Block(BLOCK_SIZE) 
    alice_init = bc.get_balance(alice)
    new_address = uuid.uuid4().hex
    b.tx(new_address, alice) 
    bc.add_block(b)
    assert bc.get_balance(alice) == alice_init, "Tx from sender with zero-balance should not change chain's state"



    "Should not allow a lower or equal block number to the last block"


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
    
    # test transactions
    test_update_state(bc, bob, alice) 
    test_validate_block(bc, bob, alice) 

