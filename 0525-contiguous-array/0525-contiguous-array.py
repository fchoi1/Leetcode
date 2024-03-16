class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # count before hand
        
        count = maxLength = 0
        countDict = {0:0}
        for i, n in enumerate(nums):
            count = count + 1 if n else count - 1
            if count in countDict:
                maxLength = max(maxLength, i - countDict[count] + 1)
            else:
                countDict[count] = i + 1
        return maxLength
        