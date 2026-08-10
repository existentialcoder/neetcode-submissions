class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                to_pop = st[len(st) - 1] if len(st) else ""
                if (ch == "}" and to_pop == "{") or (ch == ")" and to_pop == "(") or (ch == "]" and to_pop == "["):
                    st.pop()
                else:
                    return False
    
        return len(st) == 0

                        