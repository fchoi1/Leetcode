class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        perimeter = -1
        totalSum = 0
        while j < len(nums):
            if totalSum > nums[j]:
                perimeter = totalSum + nums[j]
            totalSum += nums[j]
            j += 1
        return perimeter
        