class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hp = {}

        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in hp:
                hp[sorted_st].append(st)
            else:
                hp[sorted_st] = [st]

        return list(hp.values())