class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        while l <= r:
            m = (l + r) // 2

            t = 0
            for p in piles:
                t += math.ceil(p / m)

            if t <= h: #is valid?
                r = m - 1
            else: # not valid, faster
                l = m + 1

        return l
