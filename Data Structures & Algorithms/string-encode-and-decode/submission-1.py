class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        # encode string
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            j = i
            # go while we are still looking at numbers
            while s[j] != '#':
                j += 1
            # get the numbers
            length = int(s[i:j])
            # set i to start of word
            i = j + 1
            # set j to end of word, i + length
            j = i + length
            sol.append(s[i:j])
            # have i point to the end of the work now (i + length + 1)
            i = j
        return sol
