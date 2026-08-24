class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        for c in s:
            count_s[ord(c) - ord('a')] += 1

        count_t = [0] * 26
        for c in t:
            count_t[ord(c) - ord('a')] += 1
        
        for i in range(len(count_s)):
            if count_s[i] != count_t[i]:
                return False

        return True
