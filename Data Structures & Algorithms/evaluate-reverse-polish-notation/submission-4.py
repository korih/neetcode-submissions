class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            else:
                r = st.pop()
                l = st.pop()
                v = 0
                if t == "+":
                    v = l + r
                elif t == "-":
                    v = l - r
                elif t == "/":
                    v = int(l / r)
                else:
                    v = l * r
                st.append(v)
        
        return st[0]