class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1 # This will be the current position. We start offset assuming the first element is the first buy_candidate.
        max_profit = 0 # This will be our accumulator
        buy_candidate = 0
        sell_candidate = 0

        # Loop invariant: ??
        while i < len(prices):
            if prices[i] < prices[i-1]: # if current value is less than last value, this is your new buy_candidate
                max_profit += prices[sell_candidate] - prices[buy_candidate] if sell_candidate >= buy_candidate else 0
                buy_candidate = i
                i += 1
            elif prices[i] >= prices[i-1]: # if current value is greater than last value, this is your new sell_candidate
                sell_candidate = i
                i += 1
        
        # Handle the remaining sell and buy
        max_profit += prices[sell_candidate] - prices[buy_candidate] if sell_candidate >= buy_candidate else 0
            
        return max_profit
        