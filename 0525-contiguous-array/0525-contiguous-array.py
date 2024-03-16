class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = maxLength = 0
        countDict = {0:-1}
        for i, n in enumerate(nums):
            count = count + 1 if n else count - 1
            if count in countDict:
                maxLength = max(maxLength, i - countDict[count])
            else:
                countDict[count] = i 
        return maxLength
        