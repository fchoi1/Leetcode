class Solution:
    def triangleType(self, nums: List[int]) -> str:
       
        if max(nums) >=  sum(nums) - max(nums):
            return "none"
        s = set(nums)
        if len(s) == 3:
            return "scalene"
        elif len(s) == 2:
            return "isosceles"
        elif len(s) == 1:
            return "equilateral"
        else:
            return "none"
        