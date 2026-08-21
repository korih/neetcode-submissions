class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        subset = []
        nums.sort()

        def helper(i):
            if sum(subset) == target:
                sol.append(subset.copy())
                return
            if i >= len(nums) or sum(subset) > target:
                return

            # add new
            subset.append(nums[i])
            helper(i )

            # remove 
            subset.pop()
            helper(i + 1)

        helper(0)
        return sol
