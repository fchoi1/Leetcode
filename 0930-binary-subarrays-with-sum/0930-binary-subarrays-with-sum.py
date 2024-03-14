class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        trailZeros = leadZeros = 1
        left = currSum = count = 0

        for n in nums:
            currSum += n
            if currSum > goal: 
                while nums[left] == 0:
                    leadZeros += 1
                    left += 1
                
                count += trailZeros * (trailZeros - 1) // 2  if goal == 0 else trailZeros * leadZeros
                
                currSum -= nums[left]
                left += 1
                leadZeros = 1

            trailZeros = trailZeros + 1 if n == 0 else 1

        if currSum == goal: 
            if goal == 0:
                return count + trailZeros * (trailZeros - 1) // 2
                
            while left < len(nums) and nums[left] == 0:
                leadZeros += 1
                left += 1
            count += trailZeros * leadZeros
        return count
            
