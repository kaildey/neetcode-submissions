class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price = 101
        for i in range(len(prices)):
            price = min(prices[i], price)

            if price == prices[i]:
                continue
            
            profit = prices[i] - price
            max_profit = max(max_profit, profit)
        
        return max_profit