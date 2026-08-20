class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        sol = 0
        l = 0

        # length - maxFreq <= k
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # char > count (0 if empty)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            sol = max(sol, r - l + 1)

        return sol
