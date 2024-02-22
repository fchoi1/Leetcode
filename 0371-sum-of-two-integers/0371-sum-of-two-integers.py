class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        if we create a series of 4 1's and & them to any larger size series, we will get just that part of the series we want, so

            1 1 1 1 1 0 0 1
            0 0 0 0 1 1 1 1 &
            0 0 0 0 1 0 0 1  ( Important to note that using a mask removes the two's compliment)
        '''
        mask = 0xffffffff
        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry 
        return (a & mask) if b > 0 else a
