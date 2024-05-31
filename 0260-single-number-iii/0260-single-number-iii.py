class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        # xor 
        xor = 0
        for n in nums:
            xor ^= n
        right_most = xor & -xor
        val = 0
        for n in nums:
            if (right_most & n) != 0:
                val ^= n
        return [val, val ^ xor]
