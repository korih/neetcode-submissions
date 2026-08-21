class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (d, point))
        
        count = 0
        sol = []
        while True:
            if count == k:
                break
            sol.append(heapq.heappop(heap)[1])
            count += 1
        
        return sol
