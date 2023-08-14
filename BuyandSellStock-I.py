#we buy on the day when prices is less(cud be any day in the order along the prices array and sell it on any of the day after we bought when the price is highest of all the prices
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            minprice = min(minprice,prices[i])
            profit = max(profit, prices[i] - minprice)
        return profit
        # maxprofit = 0
        # buy = prices[0]
        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         maxprofit += prices[i] - buy
        #     buy = prices[i]
        
        # return maxprofit

        
