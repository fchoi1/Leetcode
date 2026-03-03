class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        def reverse_and_invert(binary_str):
            # Invert and reverse in one go
            return ''.join('1' if b == '0' else '0' for b in reversed(binary_str))


        for _ in range(n-1):
            s = s + '1' + reverse_and_invert(s)
            
        return s[k - 1]
        