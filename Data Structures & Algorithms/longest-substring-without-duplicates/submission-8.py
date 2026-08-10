class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in ch_set:
                ch_set.remove(s[l])
                l += 1
            ch_set.add(s[r])
            res = max((r-l) + 1, res)

        return res