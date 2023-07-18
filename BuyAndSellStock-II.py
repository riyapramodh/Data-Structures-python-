#when to buy and sell the stock inorder to get maximum profit
def check(prices):#the prices array has the price of the item on each day of the week; our goal is to calculatethe max profit that can be made in the week by buying when the price is less and selling when the price is high
    total_profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
           total_profit += prices[i] - prices[i-1] #it is the diff bw the current days price and prev days price if the current day price>prev day price
    return total_profit #the sum of all such max profits made within the week is summed up to give thw total profit
