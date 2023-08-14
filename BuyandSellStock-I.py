#we buy on the day when prices is less(cud be any day in the order along the prices array and sell it on any of the day after we bought when the price is highest of all the prices
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minprice = prices[0]
       for i in range(1,len(prices)):
           check_profit = prices[i] - minprice # checking the profit that can be made
           profit = max(profit,cehck_profit) # we see if the newly calculated profit is greater or the prev calculated profit and assign that to profit
           minprice = min(minprice,prices[i]) #we check if the current ele is less value or the already stored minprice value is lesser
        return profit
        # maxprofit = 0
        # buy = prices[0]
        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         maxprofit += prices[i] - buy
        #     buy = prices[i]
        
        # return maxprofit

        
