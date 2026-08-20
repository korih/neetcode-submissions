class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            tup = (t, i)
            while stack and t > stack[-1][0]:
                t_e, i_e = stack.pop()
                sol[i_e] = i - i_e
            stack.append(tup)
        
        return sol