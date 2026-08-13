class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = []
        freq = [[] for _ in range(len(nums))]
        count = {}

        # Build the mapping
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0
        
        # Add into bucket
        # value is index
        # key is num
        print("Hi", len(freq))
        for key, value in count.items():
            freq[value].append(key)
            
        for value_list in reversed(freq):
            for val in value_list:
                if len(sol) == k:
                    return sol
                sol.append(val)
        
        return sol