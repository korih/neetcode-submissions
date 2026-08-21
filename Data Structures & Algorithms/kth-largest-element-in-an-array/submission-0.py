class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        count = 1
        for num in nums:
            if count == k:
                return num
            count += 1