class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        sol = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            # (R - L) - max_freq > k -> False
            while ((r - l + 1) - max_freq) > k:
                freq[s[l]] -= 1
                l += 1

            sol = max(sol, r - l + 1)
            
        return sol