import matplotlib.pyplot as plt
import codecs
decode_hex = codecs.getdecoder("hex_codec")

extranonce1s = []
extranonce2s = []
block_nums = []
for block in open("antpool", "r").read().splitlines()[20000:25000]:
    blocknum = block.split(",")[0]
    block_nums += [int(blocknum)]
    coinbase = block.split(",")[1].strip()
    extranonce1 = int.from_bytes(int(coinbase[-16:-8], 16).to_bytes(4, byteorder='little'), byteorder='big')
    extranonce2 = int.from_bytes(int(coinbase[-8:-2], 16).to_bytes(3, byteorder='little'), byteorder='big')
    try:
        datacenter_candidate = decode_hex(coinbase.split("627920")[1].split("20")[1])[0].decode('ascii').split("/")[0]
        datacenter_candidate = datacenter_candidate[0:3]
        print(datacenter_candidate)
    except:
        continue
    extranonce1s += [extranonce1]
    extranonce2s += [extranonce2]
    #print(coinbase[-30:-20], coinbase[-20:-16], coinbase[-16:-8], coinbase[-8:-2], coinbase[-2:], len(coinbase), extranonce1, extranonce2, blocknum)

#plt.hist(block_nums, bins=300)
plt.hist(extranonce1s, bins=800)
plt.show()
plt.hist(extranonce2s, bins=800)
plt.show()

print("Extranonce1 stats: ", min(extranonce1s), max(extranonce1s), int(sum(extranonce1s) / float(len(extranonce1s))))
print("Extranonce2 stats: ", min(extranonce2s), max(extranonce2s), int(sum(extranonce2s) / float(len(extranonce2s))))
