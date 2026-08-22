class Solution:
    def climbStairs(self, n: int) -> int:
        # 4 1111 22 112 211 121 
        # 5 11111 221 212 122 1112 1121 1211 2111
        if n == 0:
            return 0
        n_1 = 0
        n_2 = 1
        for i in range(n):
            tmp = n_2
            n_2 = n_1 + tmp
            n_1 = tmp
        
        return n_2