class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        slow = c = 0
        minKIndex = maxKIndex = -1
        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                slow = i + 1
                minKIndex = maxKIndex = -1 
                continue
           
            if n == minK:
                minKIndex = i + 1
            
            if n == maxK:
                maxKIndex = i + 1

            c += max(0, min(minKIndex, maxKIndex) - slow) 

        return c
        

        # 2 2 1 3 5 2 1

        # 2 2 1 3 5 2 
        # 2  2 1 3 5
        #    2 1 3 5
        #    2 1 3 5 2 
        #    2 1 3 5 2 1
        #      1 3 5
        #      1 3 5 2
        #      1 3 5 2 1

        #          5 2 1
        #        3 5 2 1
    
        