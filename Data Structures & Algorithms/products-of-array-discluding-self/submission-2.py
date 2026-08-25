class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        # 2 2 2 2 2
        # 1 2 4 8 16
        # x x x 16 16
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            sol[i] = sol[i] * prod

        prod = 1
        for i in range(len(nums) - 2, 0 - 1, -1):
            prod *= nums[i + 1]
            sol[i] = sol[i] * prod

        return sol
