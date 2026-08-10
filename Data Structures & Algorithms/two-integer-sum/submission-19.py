class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx_map = {}

        for idx, num in enumerate(nums):
            if target - num in num_to_idx_map:
                return [num_to_idx_map[target - num], idx]
            num_to_idx_map[num] = idx