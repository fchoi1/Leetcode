class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (2**(num.bit_length()) - 1)