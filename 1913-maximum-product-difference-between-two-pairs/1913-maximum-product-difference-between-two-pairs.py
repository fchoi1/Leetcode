class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w,x,y,z = sorted(nums[:4])

        for n in nums[4:]:
            if n > z:
                y,z = z, n
            elif n < w:
                w,x = n,w 
            elif n < x:
                x = n
            elif n > y:
                y = n
        return y * z -  w * x
                
