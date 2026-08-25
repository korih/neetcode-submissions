class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []

        s_map = {}
        for s in strs:
            s_arr = [0] * 26
            for c in s:
                s_arr[ord(c) - ord('a')] += 1
            
            s_tup = tuple(s_arr)
            if s_tup in s_map:
                s_map[s_tup].append(s)
            else:
                s_map[s_tup] = [s]
        
        for key, value in s_map.items():
            sol.append(value)

        return sol