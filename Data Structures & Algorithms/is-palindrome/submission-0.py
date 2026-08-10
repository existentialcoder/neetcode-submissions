class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_lower = [ch for ch in list(s_lower) if ch.isalnum()]

        start = 0
        end = len(s_lower) - 1

        print("".join(s_lower))

        while (start < end):
            if s_lower[start] != s_lower[end]:
                return False
            start += 1
            end -= 1

        return True

