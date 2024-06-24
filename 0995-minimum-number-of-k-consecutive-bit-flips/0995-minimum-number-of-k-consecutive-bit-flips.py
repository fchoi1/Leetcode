import sys
sys.set_int_max_str_digits(0)

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # 0
        # xor 
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

        # [1,1,0,1,0,1,1,0,0]
        #  1 1 1 0 0 1 1 0 0
        # 1 1 1  1 1 1 1 0 0
        # 1 1 1 1 1 1 1 1 1
        if currNum < limit:
            counts += 1
            currNum ^= xor

        while i < len(nums):
            if currNum == xor:
                while i < len(nums) and nums[i] == 1:
                    currNum = currNum << 1 & xor
                    currNum |= nums[i]
                    i += 1
                if i >= len(nums):
                    break
            if currNum < limit:
                currNum = currNum ^ xor
                counts += 1
            currNum = currNum << 1 & xor
            currNum |= nums[i]
            i += 1

        if currNum == 0:
            counts += 1
            currNum = xor
        print("Done", currNum, counts)
        return counts if currNum == xor else -1