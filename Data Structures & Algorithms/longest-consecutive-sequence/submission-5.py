class Solution:
    # how would i solve this if it was just longest consecutive sequence in order?
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen_set = set()
        for n in nums:
            seen_set.add(n)

        sol = 0
        for n in seen_set:
            if n - 1 in seen_set:
                continue

            count = 0
            curr = n
            while curr in seen_set:
                curr += 1
                count += 1

            
            sol = max(sol, count)
        
        return sol
        