prices = [1,3,7,5,10,3]
fee = 3
 
n = len(prices)
hold = -prices[0]  # max cash today if we hold a stock
cash = 0  # max cash today if we dont hold any stock

cashes = []
holds = []
cashes.append(cash)
holds.append(hold)

for i in range(1, n):
    cash = max(cash, prices[i] - hold - fee)  # max(keep cash, sell yesterday's holding on today)
    hold = max(hold, cash - prices[i])  # max(hold stock, use yesterday's cash to buy today's stock)
    cashes.append(cash)
    holds.append(hold)

print('cashes = ', cashes)
print('holds = ', holds)