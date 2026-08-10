class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            computed_area = (r - l) * min(heights[l], heights[r])

            max_area = max(max_area, computed_area)

            if heights[l] == min(heights[l], heights[r]):
                l +=1
            else:
                r -= 1

        return max_area