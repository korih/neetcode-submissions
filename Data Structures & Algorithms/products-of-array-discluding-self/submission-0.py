class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go through array once forward and backwards
        # on each pass put the cumulated multiple in that cell
        sol = [1] * len(nums)
        multiple = 1
        for i, num in enumerate(nums):
            sol[i] *= multiple
            multiple *= num

        multiple = 1
        i = len(nums) - 1
        for num in reversed(nums):
            sol[i] *= multiple
            multiple *= num
            i -= 1

        return sol