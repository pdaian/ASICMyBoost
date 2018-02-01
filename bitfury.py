from matplotlib import pyplot as plt
from util import *

extranonce1s = []
extranonce2s = []
blocks = open("bitfury", "r").read().splitlines()
print(len(blocks))

failed = 0
for block in blocks:
    try:
        blocknum = block.split(",")[0]
        coinbase = block.split(",")[1].strip()
        if not "2f426974" in coinbase:
            failed += 1
            continue
        coinbase = coinbase.split("2f426974")[0]
        #extranonce1 = int.from_bytes(int(coinbase[-6:], 16).to_bytes(3, byteorder='little'), byteorder='big')
        extranonce2 = int.from_bytes(int(coinbase[-8:-2], 16).to_bytes(3, byteorder='little'), byteorder='big')
        extranonce2 = int(coinbase[-8:-2], 16)
        #extranonce1s += [extranonce1]
        extranonce2s += [extranonce2]
        extranonce1 = 0
        #print(coinbase[11:-29].replace("0", " "), len(coinbase), extranonce1, extranonce2, blocknum)
        print(coinbase.replace("0", " ")[:-2], coinbase.replace("0", " ")[-8:-2], extranonce2)
    except:
        pass

print("Failed", failed)
plt.hist(extranonce2s, bins=100)
plt.show()
kde(extranonce2s, 'b')
plt.show()


#print("Extranonce1 stats: ", min(extranonce1s), max(extranonce1s), int(sum(extranonce1s) / float(len(extranonce1s))))
print("Extranonce2 stats: ", min(extranonce2s), max(extranonce2s), int(sum(extranonce2s) / float(len(extranonce2s))))
