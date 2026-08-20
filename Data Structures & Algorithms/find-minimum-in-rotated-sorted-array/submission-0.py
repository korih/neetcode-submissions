class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if l < r then l has to be the sol
        if nums[0] < nums[-1]:
            return nums[0]
        # else binary search
        # if m > r must be l = m + 1
        # if m < l must be r = m - 1
        # we break when ==
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m 
        
        return nums[l]