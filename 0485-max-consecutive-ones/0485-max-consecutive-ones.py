class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = ones = 0
        for n in nums:
            if n == 1:
                ones += 1
            else:
                ones = 0
            maxOnes = max(maxOnes, ones)
        return maxOnes