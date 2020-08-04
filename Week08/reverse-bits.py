class Solution:
    def reverseBits(self, n: int) -> int:
        res, index = 0, 31
        while n:
            res += (n & 1) << index
            n = n >> 1
            index -= 1
        return res
