class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        heap = stones

        while len(heap) > 1:
            # have to add all to heap
            stone1 = heapq.heappop_max(heap)
            stone2 = heapq.heappop_max(heap)
            if stone1 == stone2:
                continue
            else:
                stone3 = stone1 - stone2
                heapq.heappush_max(heap, stone3)
        
        return 0 if len(heap) == 0 else heap[0]