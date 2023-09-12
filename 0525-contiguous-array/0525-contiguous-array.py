class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumDict = {0: -1}
        maxLen = 0
        total =  0
        for i, val in enumerate(nums):
            total += val if val == 1 else -1
            if total in sumDict:
                maxLen = max(maxLen,  i - sumDict[total])
            else:
                sumDict[total] = i
        print(sumDict)
        return maxLen


        