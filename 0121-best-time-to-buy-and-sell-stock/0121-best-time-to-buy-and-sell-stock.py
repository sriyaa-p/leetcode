class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return max profit else return 0 
        lengthprices = len(prices)
        buyprice = prices[0]
        maxprofit = 0
        #find the day with lowest value
        for i in range (lengthprices):
            if prices[i]<buyprice:
                buyprice = prices[i]
            else:
                profit = prices[i]-buyprice
                maxprofit = max(maxprofit,profit)
        return maxprofit