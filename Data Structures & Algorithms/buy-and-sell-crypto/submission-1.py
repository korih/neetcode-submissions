class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        min_so_far = prices[0]
        
        for i in range(1, len(prices)):
            sol = max(sol, prices[i] - min_so_far)

            if prices[i] < min_so_far:
                min_so_far = prices[i]
            

        return sol
                