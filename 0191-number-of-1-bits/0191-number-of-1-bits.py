class Solution:
    def hammingWeight(self, n: int) -> int:
        # One liner: str(bin(n)).count('1')
        # Proper way:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count