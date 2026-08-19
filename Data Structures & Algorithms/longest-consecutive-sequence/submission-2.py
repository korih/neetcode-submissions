class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        sol = 0

        for num in nums:
            if not mp[num]: #almost always, new number
                # left + right + 1, joining sequence
                mp[num] = mp[num - 1] + mp[num + 1] + 1

                # the beginning of the sequence should have the num too
                mp[num - mp[num - 1]] = mp[num]

                # the ending of the sequence updated to new value
                mp[num + mp[num + 1]] = mp[num]

                sol = max(sol, mp[num])
        
        return sol