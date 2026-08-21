class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # no sorting
        # can do heap? just add it all?
        arr = [-x for x in nums]
        heapq.heapify(arr)
        for i in range(len(arr)):
            val = heapq.heappop(arr)
            if i + 1 == k:
                return -val