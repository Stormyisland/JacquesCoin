from Block import Block


blockchain = []

genesis_block = Block("My genesis block", ["Satoshi sent 1 BTC KING!", 
                                        "Satoshi sent 2 BTC lord",
                                        "Satoshi sent 3 BTC GOD!"])

second_block = Block(genesis_block.block_hash,["Satoshi sent 3 BTC theodore!"
                                            "Satoshi sent 3 BTC jacques!"
                                            "Satoshi sent 3 BTC to bill!"])

third_block =Block(second_block.block_hash, ["Satoshi sent 300 BTC theodore!"
                                            "Satoshi sent 600  BTC jacques!"
                                            "Satoshi sent 30 BTC to billy!"])

print("Block hash: Genesis Block 1")
print(genesis_block.block_hash)

print("Block hash: Second Block 2")
print(second_block.block_hash)

print("Block hash: Third_block 3")
print(third_block.block_hash)









#hash = hashlib.sha256("secret message" .encode()).hexdigest()
#print(hash)