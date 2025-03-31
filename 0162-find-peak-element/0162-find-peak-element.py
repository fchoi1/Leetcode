class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        m = 0

        for i in range(len(nums)):
            if nums[i] > nums[m]:
                m = i
        
        return m