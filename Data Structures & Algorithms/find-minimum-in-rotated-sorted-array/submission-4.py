class Solution:
    def findMin(self, nums: List[int]) -> int:
        # pivot, two arrays, keep res value
        # if l < r then l is sol
        # elif l < m then look right
        # else look left

        sol = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                return min(sol, nums[l])

            m = (l + r) // 2
            sol = min(nums[m], sol)
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return sol
