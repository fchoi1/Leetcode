class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        totalSum = ((n+1)*(n))/2
        for i in nums:
            sum+=i
        return int(totalSum - sum)

        