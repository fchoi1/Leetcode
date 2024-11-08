class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        target = 2 ** (maximumBit) - 1
        prefix = []
        curr = 0
        for n in nums:
            curr ^= n
            prefix.append(curr ^ target)
        
        # print(prefix[::-1])
        # print(0 ^ 1 ^ 1 ^ 3 ^ 3)
        # print(0 ^ 1 ^ 1 ^ 3)
        # print(0 ^ 1  ^ 3)
        # print(0 ^ 3)
        return prefix[::-1]