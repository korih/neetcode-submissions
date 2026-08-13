class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {} = 
        # Go through list, creating a tuple of letter:count in alpha ord
        # Map each of these tuples with original word
        # then go through each of these mappings and create list
        sol = []
        mapping = {}

        for wrd in strs:
            c_table = [0] * 26
            for c in wrd:
                c_table[ord(c) - ord('a')] += 1

            key = tuple(c_table)
            if key in mapping:
                mapping[key].append(wrd)
            else:
                mapping[key] = [wrd]

        for key, value in mapping.items():
            sol.append(value)
        
        return sol