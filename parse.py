from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import math
import codecs
decode_hex = codecs.getdecoder("hex_codec")
ALL_DCS = ['xz0', 'bj8', 'bj5', 'yn1', 'wy', 'sc7', 'sc2', 'bj7', 'bj1', 'dq', 'sc9', 'sc8', 'sz0', 'sc3', 'sc0', 'sc4', 'sc5', 'bj6', 'nm0', 'il0', 'usa', 'sc1', 'bj0']

#plt.style.use('seaborn-deep')

def kde(data, color):
        kde = gaussian_kde( data )
        # these are the values over wich your kernel will be evaluated
        dist_space = linspace( min(data), max(data), 1000 )
        # plot the results
        plt.plot( dist_space, kde(dist_space) , color = color)

en3s = []
colors = []
blocks_and_en3s = []
dcs = {}
#for blockrange in ((9000, 10000, 'yellow'), (19000, 20000, 'purple'), (21000, 22000, 'r'), (22000, 23000, 'g'), (23000, 24000, 'b'), (24000, 25000, 'pink')):
for blockrange in ((0, 9000, 'r'), (9000, 14000, 'g'), (14000, 18000, 'b'), (18000, 22000, 'black'), (22000, 26000, 'purple')):
    en1 = []
    en2 = []
    en3 = []
    en4 = []
    en5 = []
    blocks = open('antpool').read().splitlines()[blockrange[0]:blockrange[1]]
    for block in blocks:
        blocknum = int(block.split(",")[0])
        coinbase = block.split(",")[1]
        if coinbase.strip()[-2:] != '00':
            continue # (uncomment to remove "nonstandard")
            en5 += [int(coinbase.strip()[-2:], 16)]
            #print(coinbase.strip()[-2:])
        e1 = int(coinbase.strip()[-8:-2], 16)
        e2 = int(coinbase.strip()[-16:-8], 16)
        e3 = int.from_bytes(e1.to_bytes(3, byteorder='little'), byteorder='big')
        e4 = int.from_bytes(e2.to_bytes(4, byteorder='little'), byteorder='big')
        try:
            datacenter_candidate = decode_hex(coinbase.split("627920")[1].split("20")[1])[0].decode('ascii').split("/")[0]
            datacenter_candidate = datacenter_candidate[0:3]
            dcs[datacenter_candidate] = dcs.get(datacenter_candidate, []) + [(blocknum, e3)]
        except:
            pass
        en1 += [e1]
        en2 += [e2]
        en3 += [e3]
        blocks_and_en3s += [(blocknum, e3)]
        en4 += [e4]
        print(coinbase.strip()[-16:-8], coinbase.strip()[-8:-2], coinbase.strip()[-2:], len(coinbase))

    print(len(en3), min(en3), max(en3), int(sum(en3) / float(len(en3))))
    print(len(en4), min(en4), max(en4), int(sum(en4) / float(len(en4))))
    print()
    en3s += [en3]
    colors += blockrange[2]
    #kde(en3, blockrange[2])

    #plt.hist(en3, bins=100)
    #plt.show()
    #plt.hist(en5, bins=100)
    #plt.show()

#for dc in ALL_DCS:
#    print(dc, len(dcs[dc]))

def draw_trend(x, y, start, end, color):
    if end is -1:
        end = len(x)
    plt.plot(np.unique(x)[start:end], np.poly1d(np.polyfit(x[start:end], y[start:end], 1))(np.unique(x[start:end])), color=color)

def get_coords(blocks_and_en3s):
    x = [x[0] for x in blocks_and_en3s]
    LOG_SCALE = False
    if LOG_SCALE:
        y = [0 if x[1] == 0 else math.log(x[1],10) for x in blocks_and_en3s]
    else:
        y = [x[1] for x in blocks_and_en3s]
    return (x, y)

(x, y) = get_coords(blocks_and_en3s)
#(x, y) = get_coords(dcs['usa'])
plt.scatter(x, y, color='g')
#(x, y) = get_coords(dcs['bj1'])
#plt.scatter(x, y)
draw_trend(x, y, 0, -1, 'r')
for start in range(0, len(x), 2000):
    draw_trend(x, y, start, start + 2000, 'black')
for start in range(0, len(x), 5000):
    draw_trend(x, y, start, start + 5000, 'green')
for start in range(0, len(x), 10000):
    draw_trend(x, y, start, start + 10000, 'purple')
plt.show()

exit(0)

plt.show()
plt.hist(en3s, bins=100, alpha=0.7, label=[str(x) for x in range(1, len(en3s) + 1)], normed=True)
plt.legend(loc='upper right')
plt.show()
exit(0)

#plt.hist(en1, bins=100)
#plt.show()
#plt.hist(en2, bins=100)
#plt.show()
#plt.hist(en3, bins=100)
#plt.show()
#plt.hist(en4, bins=100)
#plt.show()
