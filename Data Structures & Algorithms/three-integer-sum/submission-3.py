class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        print(nums)
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m, r = l + 1, len(nums) - 1

            while m < r:
                res = nums[l] + nums[m] + nums[r]
                if res < 0:
                    m += 1
                elif res > 0:
                    r -= 1
                else:
                    sol.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m - 1] == nums[m]:
                        print(m)
                        m += 1
        
        return sol