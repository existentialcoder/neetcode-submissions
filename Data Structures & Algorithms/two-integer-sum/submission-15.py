class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx_map = {}

        for idx, num in enumerate(nums):
            num_to_idx_map[num] = idx

        for idx, num in enumerate(nums):
            if target - num in num_to_idx_map and idx != num_to_idx_map[target - num]:
                return [idx, num_to_idx_map[target - num]]