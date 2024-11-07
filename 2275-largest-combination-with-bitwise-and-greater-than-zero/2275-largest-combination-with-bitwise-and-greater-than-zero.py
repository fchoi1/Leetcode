class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        max_bits = 24
        bits = [0] * max_bits
        for n in candidates:
            for bit in range(max_bits):
                if n & (1 << bit):  
                    bits[bit] += 1
        return max(bits)