from matplotlib import pyplot as plt
INTERVAL = 1000

pool_shares = {}
pool_data = {}
pool_data_raw = open("pools", "r").read().splitlines()
for block in pool_data_raw:
        block = block.split("`")
        pool_data[int(block[0])] = block[-1]
        pool_shares[block[-1]] = []


curr_block = INTERVAL
while curr_block in pool_data:
    print(curr_block)
    round_stats = {}
    for block in range(curr_block-INTERVAL, curr_block):
        pool = pool_data[block]
        if pool in round_stats:
            round_stats[pool] += 1
        else:
            round_stats[pool] = 1
    for pool in pool_shares.keys():
        if pool in round_stats:
            pool_shares[pool] += [round_stats[pool]]
        else:
            pool_shares[pool] += [0]
    curr_block += INTERVAL


plt.plot(list(range(0, len(pool_shares['antpool']))), pool_shares['antpool'], color='b')
plt.plot(list(range(0, len(pool_shares['btcc']))), pool_shares['btcc'], color='r')
plt.plot(list(range(0, len(pool_shares['btcc']))), pool_shares['bitfury'], color='g')
plt.plot(list(range(0, len(pool_shares['btcc']))), pool_shares['slush'], color='purple')
plt.plot(list(range(0, len(pool_shares['btcc']))), pool_shares['discusfish'], color='black')
plt.show()
