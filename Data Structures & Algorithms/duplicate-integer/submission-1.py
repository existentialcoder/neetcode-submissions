class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_set = set()
        result = False

        for num in nums:
            if num in visited_set:
                result = True
                break
            else:
                visited_set.add(num)

        return result
