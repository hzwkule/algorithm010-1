class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def form_check_dict(string: str):
            c = {}
            for i in string:
                if i in c: c[i] += 1
                else: c[i] = 1
            return c
        c1 = c2 = {}
        c1 = form_check_dict(s)
        c2 = form_check_dict(t)
        return (c1 == c2)
