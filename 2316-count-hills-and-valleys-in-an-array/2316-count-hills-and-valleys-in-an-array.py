class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[0]
        for i in range(1,len(nums)-1):

            if nums[i] == nums[i + 1]:
                continue
            
            if (nums[i] > prev and nums[i] > nums[i+1]) or (nums[i] < prev and nums[i] < nums[i+1]):
                ans += 1
            
            prev = nums[i]
        
        return ans
            
        