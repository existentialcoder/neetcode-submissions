class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        for idx, num in enumerate(nums):
            num_index_map[num] = idx

        for idx, num in enumerate(nums):
            if (target - num) in nums and idx != num_index_map[target-num]:
                return [idx, num_index_map[target - num]]