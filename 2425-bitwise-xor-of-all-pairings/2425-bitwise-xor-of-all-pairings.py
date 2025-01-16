class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # odd number of ones
        N1 = len(nums1)
        N2 = len(nums2)

        bits = [0] * 30 # 10^9 30 bits

        xor_1 = 0
        xor_2 = 0

        
        for n in nums1:
            xor_1 ^= n
        
        for n in nums2:
            xor_2 ^= n
        print(N1, N2, xor_1, xor_2)
        if N2 % 2 == 0:
            xor_1 = 0

        if N1 % 2 == 0:
            xor_2 = 0
        print("Done",N1, N2, xor_1, xor_2)
        
        return xor_1 ^ xor_2