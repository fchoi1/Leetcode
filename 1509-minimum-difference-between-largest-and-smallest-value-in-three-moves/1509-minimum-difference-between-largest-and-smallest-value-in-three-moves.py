class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        maxArr = [-inf] * 4
        minArr = [inf] * 4


        for n in nums:
            if n > maxArr[0]:
                maxArr[0],maxArr[1],maxArr[2],maxArr[3] = n,maxArr[0],maxArr[1],maxArr[2]
            elif n > maxArr[1]:
                maxArr[1],maxArr[2],maxArr[3] = n,maxArr[1],maxArr[2]
            elif n > maxArr[2]:
                maxArr[2],maxArr[3] = n,maxArr[2]
            elif n > maxArr[3]:
                maxArr[3] = n

            if n < minArr[0]:
                minArr[0],minArr[1],minArr[2],minArr[3] = n,minArr[0],minArr[1],minArr[2]
            elif n < minArr[1]:
                minArr[1],minArr[2],minArr[3] = n,minArr[1],minArr[2]
            elif n < minArr[2]:
                minArr[2],minArr[3] = n,minArr[2]
            elif n < minArr[3]:
                minArr[3] = n
            
        return min(maxArr[0] - minArr[3], maxArr[1] - minArr[2], maxArr[2] - minArr[1], maxArr[3] - minArr[0])