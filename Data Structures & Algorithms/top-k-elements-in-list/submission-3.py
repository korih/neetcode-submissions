class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)
        
        for key, value in freq_map.items():
            freq_arr[value].append(key)
        
        sol = []
        i = len(freq_arr) - 1
        while len(sol) < k:
            for n in freq_arr[i]:
                sol.append(n)
            i -= 1
            
        return sol