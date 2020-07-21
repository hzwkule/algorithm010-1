class Solution:
    ugly = sorted(2**i2*3**i3*5**i5 for i2 in range(32) for i3 in range(32) for i5 in range(32))
    def nthUglyNumber(self, n: int) -> int:
        # ugly = [1]
        # i = j = k = 0
        # while len(ugly) < n:          
        #     while ugly[i] * 2 <= ugly[-1]: i += 1
        #     while ugly[j] * 3 <= ugly[-1]: j += 1
        #     while ugly[k] * 5 <= ugly[-1]: k += 1
        #     ugly.append(min(ugly[i] * 2, ugly[j] * 3, ugly[k] * 5))
        # return ugly[-1]

        
        return self.ugly[n-1]
