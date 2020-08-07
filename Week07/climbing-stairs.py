class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2, res = 1, 2, n
        if n > 2:
            for i in range(2,n):
                res = f1 + f2
                f1, f2 = f2, res
        return res
