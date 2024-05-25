from Block import Block


blockchain = []

genesis_block = Block("My genesis block", ["Satoshi is KING!", 
                                        "Satoshi is lord",
                                        "Satoshi is GOD!"])

print(genesis_block.block_hash)










#hash = hashlib.sha256("secret message" .encode()).hexdigest()
#print(hash)