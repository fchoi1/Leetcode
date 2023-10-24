class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = total = nums[0]
        for n in nums[1:]:
            if currSum <= 0:
                currSum = n
            else:
                currSum += n
            total = max(total, currSum)
        return total
        