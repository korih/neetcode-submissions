class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # same as previous, just looking for target
        # one side is always sorted, we need
        # to see which one is sorted

        # if left is sorted, we can ask
        # if target is here then look left else go right

        # if left is not sorted, right is sorted, we can ask 
        # the same question just vice versa

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1 
        
        return -1