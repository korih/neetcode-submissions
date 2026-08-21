class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
        
        mx = (0, 0)
        for key, value in mp.items():
            if mx[1] < value:
                mx = (key, value)
        
        return mx[0]