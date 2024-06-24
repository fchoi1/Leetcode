import sys
sys.set_int_max_str_digits(0)

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if k == 1:
            return Counter(nums)[0]

        currNum = 0
        for i, n in enumerate(reversed(nums[:k])):
            if n:
                currNum += 2 ** i
        counts = 0
        xor = 2 ** k - 1
        limit = 2 ** (k - 1)
        i = k
        if currNum < limit:
            counts += 1
            currNum ^= xor

        while i < len(nums):
            if currNum < limit:
                currNum = currNum ^ xor
                counts += 1
            currNum = currNum << 1 & xor
            currNum |= nums[i]
            i += 1

        if currNum == 0:
            counts += 1
            currNum = xor
        return counts if currNum == xor else -1