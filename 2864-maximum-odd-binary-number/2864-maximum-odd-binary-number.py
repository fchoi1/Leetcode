class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        odd = ''
        for i in range(len(s) - 1):
            if i < ones - 1:
                odd += '1'
            else:
                odd += '0'
        return odd + '1'

        