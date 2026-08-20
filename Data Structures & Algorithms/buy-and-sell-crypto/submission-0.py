class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        sol = 0

        for price in prices:
            if smallest > price:
                curr = price - smallest
                sol = max(curr, sol)
                smallest = price
            else:
                curr = price - smallest
                sol = max(curr, sol)
        
        return sol