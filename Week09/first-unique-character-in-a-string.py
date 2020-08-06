class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = collections.defaultdict()
        for i in s:
            if i not in t:
                t[i] = 1
            else:
                t[i] += 1
        for i in range(len(s)):
            if t[s[i]] == 1:
                return i
        return -1
