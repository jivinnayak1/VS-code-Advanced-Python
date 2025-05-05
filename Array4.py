stocks_price = [100,200,300,400,120,450,500,240,370]

profit = 0

for i in range(1,len(stocks_price)):
    if(stocks_price[i]>stocks_price[i-1]):
        profit = profit+(stocks_price[i]-stocks_price[i-1])


    if(stocks_price[i]<stocks_price[i-1]):
        profit = profit-(stocks_price[i-1]-stocks_price[i])

print(profit)

stock_Price = [100,200,150,300,400,500,190]
