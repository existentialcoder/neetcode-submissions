class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp_t = list(t)

        for ch in s:
            if ch not in temp_t:
                return False
            temp_t.remove(ch)

        return True
