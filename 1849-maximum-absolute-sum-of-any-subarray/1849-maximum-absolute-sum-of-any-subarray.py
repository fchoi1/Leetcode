class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        currSum = currMin = currMax = 0
        
        for n in nums:
            currSum += n
            currMax = max(currSum, currMax)
            currMin = min(currSum, currMin)
        return currMax - currMin
        