class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        c = 0
        slow = minKIndex = maxKIndex = -1
        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                slow = i 
                minKIndex = maxKIndex = -1 
                continue
           
            if n == minK:
                minKIndex = i 
            
            if n == maxK:
                maxKIndex = i 

            c += max(0, min(minKIndex, maxKIndex) - slow) 

        return c
        