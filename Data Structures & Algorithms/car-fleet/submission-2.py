class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the list based on speed and position
        # now iterate, keep a stack for the times
        # if there are two items of the same time 
        # then you pop it. Also guard the stack from bad checks
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target - p) / s)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)