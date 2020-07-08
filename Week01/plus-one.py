class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        while n > 0:
            n -= 1
            if digits[n] >= 9:
                digits[n] = 0
            else:
                digits[n] += 1
                return digits
        digits.insert(0,1)
        return digits
