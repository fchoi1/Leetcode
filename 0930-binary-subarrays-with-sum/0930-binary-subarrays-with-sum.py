class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        l = 0
        count = 0
        subarrays = 0
        trailing = 0

        for i,n in enumerate(nums):
            count += n
            
            while count > goal:
                if not goal:
                    trailing -= 1
                subarrays += trailing + 1
                count -= nums[l]
                l += 1

            if n == 0:
                trailing += 1
            else:
                trailing = 0
                
        while l < len(nums) and count == goal:
            if not goal:
                trailing -= 1
            subarrays += trailing + 1
            count -= nums[l]
            l += 1

        return subarrays



