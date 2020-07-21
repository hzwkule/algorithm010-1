class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = tuple(sorted(s))
            d[ss] = d.get(ss, []) + [s]
        return list(d.values())
