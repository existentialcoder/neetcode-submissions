class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for ch in list(s):
            s_map[ch] = s_map.get(ch, 0) + 1
        
        for ch in list(t):
            t_map[ch] = t_map.get(ch, 0) + 1

        for ch in list(s):
            if s_map.get(ch, 0) != t_map.get(ch, 0):
                return False
        
        return True