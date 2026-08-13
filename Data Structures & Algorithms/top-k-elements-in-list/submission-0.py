class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap?
        # map is easy but slow
        mapp = {}

        for num in nums:
            if num in mapp:
                mapp[num] += 1
            else:
                mapp[num] = 1
        
        return sorted(mapp, key=mapp.get)[-k:]