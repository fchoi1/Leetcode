class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        N = len(nums)
        total = 0

        for i in range(N):
            currMax = nums[i]
            currMin = nums[i]
            for j in range(i + 1, N):
                currMax = max(currMax, nums[j])
                currMin = min(currMin, nums[j])
                total += currMax - currMin   
        return total