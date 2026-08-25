class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("$")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] != "$":
                    j += 1
                else:
                    break
            
            num = s[i:j]
            length = int(num)
            start = j + 1
            end = start + length
            substring = s[start:end]
            res.append(substring)
            i = end
        
        return res
