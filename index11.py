prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = []

for i in prices:
    if i>0:
        new_prices.append(i)
    else:
        new_prices.append(0)
print(new_prices)