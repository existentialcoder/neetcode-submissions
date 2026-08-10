class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_mapper = {}

        
        for idx, num in enumerate(nums):
            idx_mapper[num] = idx

        for idx, num in enumerate(nums):
            num_to_check = target - num
            idx_to_check = idx_mapper.get(num_to_check, -1)

            if idx_to_check >= 0 and idx_to_check != idx:
                return [idx, idx_to_check]