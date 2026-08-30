class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at both ends, calculate the size
        # move the pointer of the smallest height
        l, r = 0, len(heights) - 1
        sol = 0
        while l < r:
            res = min(heights[l], heights[r]) * (r - l)
            sol = max(sol, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return sol
