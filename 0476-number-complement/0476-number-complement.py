class Solution:
    def findComplement(self, num: int) -> int:
        val = num ^ (2 ** num.bit_length() - 1 )
        print(bin(val))
        return val