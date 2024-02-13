class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        tracker = [(1,-1)] * len(nums)
        largestSize = 0
        largestIndex = 0
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    size, index = tracker[j]
                    if size + 1 > largestSize:
                        largestSize = size + 1
                        largestIndex = i
                    if size+1 > tracker[i][0]:
                        tracker[i] = (size+1, j)

        res = []
        while largestIndex != -1:
            res.append(nums[largestIndex])
            largestIndex = tracker[largestIndex][1]

        return res



            
        