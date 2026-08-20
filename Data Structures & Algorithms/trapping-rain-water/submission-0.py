class Solution:
    def trap(self, height: List[int]) -> int:
        # all that matter are the highest hills
        # just look for those guys? and try to 
        # find the new max inside of them

        l = 0
        r = len(height) - 1
        sol = 0

        l_max = 0
        r_max = 0
        while l < r:
            l_val = height[l]
            r_val = height[r]

            if l_val < r_val:
                l += 1
                l_max = max(l_max, l_val)
                sol += l_max - l_val
            else:
                r -= 1
                r_max = max(r_max, r_val)
                sol += r_max - r_val

        return sol
