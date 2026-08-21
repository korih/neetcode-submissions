class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        subset = []

        def helper(i): # index to look at
            # base case
            if i >= len(nums):
                # if we reach this, we terminate our branch we have reached end
                # this is a solution
                sol.append(subset.copy())
                return
            
            # append our current nums to the list
            # this is the left case
            subset.append(nums[i])
            helper(i + 1)

            # remove our current value, then look right
            subset.pop()
            helper(i + 1)

        helper(0)
        return sol