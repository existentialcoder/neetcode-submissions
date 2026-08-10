class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        sorted_hm_list = sorted(list(hm.items()), key=lambda x: x[1], reverse=True)
        return [tup[0] for tup in sorted_hm_list[:k]]
