class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def getMax(start, end):
            last2 = last1 = maxCash = 0
            for n in nums[start:end]:
                maxCash = max(last2 + n, last1)
                last2 = last1
                last1 = maxCash
            return maxCash
        return max(getMax(0,len(nums)-1), getMax(1,len(nums)))
        