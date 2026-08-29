class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for l in range(len(nums)):
            if nums[l] > 0:
                break

            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m = l + 1
            r = len(nums) - 1

            while m < r:
                res = nums[l] + nums[m] + nums[r]
                if res == 0:
                    sol.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
                elif res > 0:
                    r -= 1
                else:
                    m += 1
        
        return sol