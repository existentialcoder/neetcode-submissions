class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        return [x[0] for x in sorted(list(hmap.items()), key=lambda x: x[1], reverse=True)[:k]]