from matplotlib import pyplot as plt

extranonce1s = []
extranonce2s = []
zeros = 16
blocks = open("btcc", "r").read().splitlines()[12000:]
blocks.reverse()
for block in blocks:
    try:
        blocknum = block.split(",")[0]
        coinbase = block.split(",")[1].strip()
        if not zeros * "0" in coinbase:
            zeros = 14
        en1_text= coinbase.replace("0" * zeros, "|").split("|")[1][8:14]
        extranonce1 = int.from_bytes(int(en1_text, 16).to_bytes(3, byteorder='little'), byteorder='big')
        extranonce2 = int.from_bytes(int(coinbase[-100:-94], 16).to_bytes(3, byteorder='little'), byteorder='big')
        extranonce1s += [extranonce1]
        extranonce2s += [extranonce2]
        print(en1_text)
        print(coinbase[8:-76].replace("0", " "), coinbase[-81:-76], len(coinbase), extranonce1, extranonce2, blocknum)
    except:
        pass

plt.hist(extranonce2s, bins=300)
plt.show()


print("Extranonce1 stats: ", min(extranonce1s), max(extranonce1s), int(sum(extranonce1s) / float(len(extranonce1s))))
print("Extranonce2 stats: ", min(extranonce2s), max(extranonce2s), int(sum(extranonce2s) / float(len(extranonce2s))))
