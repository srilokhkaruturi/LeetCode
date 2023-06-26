class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = -1
        for i in range(0, len(prices)):
            if smallest > prices[i]:
                smallest = prices[i]
            else:
                
                possible_profit = prices[i] - smallest
                
                if possible_profit > max_profit:
                    max_profit = possible_profit
                    
        return max_profit