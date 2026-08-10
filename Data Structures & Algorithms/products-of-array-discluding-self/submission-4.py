class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        product = math.prod(nums)

        product_without_0 = 1

        for num in nums:
            if num == 0: continue
            product_without_0 *= num

        product = math.prod(nums)
        
        return [int(product/num) if num!=0 else product_without_0 for num in nums]
