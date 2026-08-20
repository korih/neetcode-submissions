class Solution:
    def isValid(self, s: str) -> bool:
        # add opening chars to stack
        # if we find a closing char, find mapping
        # and pop from stack. if not correct the false

        st = []
        mp = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in mp:
                if not st:
                    return False
                else:
                    top = st.pop()
                    if top != mp[c]:
                        return False
            else:
                st.append(c)
        
        return len(st) == 0