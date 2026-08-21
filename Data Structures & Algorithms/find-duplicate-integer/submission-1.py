class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # because its 1, n we can use the values as
        # indicies. 
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        return -1