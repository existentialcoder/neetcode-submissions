class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for st in strs:
            sorted_st = "".join(sorted(st))

            if sorted_st in hmap:
                hmap[sorted_st].append(st)
            else:
                hmap[sorted_st] = [st]

        return list(hmap.values())