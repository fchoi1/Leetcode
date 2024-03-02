class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(0, len(nums)-2):
            a,b,c = nums[i:i+3]
            if a < (b + c):
                return a + b + c
        return 0
        