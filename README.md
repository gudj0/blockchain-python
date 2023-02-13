## Blockchain Implementation in Python
The following contains a Python implementation of the Level 2 blockchain. 

#### Implementation 
The implementation consists of three files:

* `blockchain.py`. 
* `block.py`

and a main program:

* `main.py`


#### Tests
There are two unit-test files: 

* `block_test.py` tests the transaction functionality
* `blockchain_test.py` tests the `add_block` and `validate_block` functionality. 

#### Depdendencies
`collections.defaultdict` and `uuid` are the two only dependencies, both of which which are standard lib. 

### How to run 
The main executable is in main.py. so just run `$ python3 main.py` to see an initial run of the transactions. Feel free to add commands in the `main` function to try out my implementation.  

You can run all tests by running: 
 
```python3 block_test.py && python3 blockchain_test.py```
