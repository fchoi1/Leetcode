class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, added, index = 1, 0, 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                added += 1
        return added


        
        # 1 2 4 8 16
        # 1 2 3 7, 14, 28

        # 1, 2, 3, 13, 23, 123, 7, 17, 27, 37, 137, 237, 1237, 


        # 
        # binary?

        # 0001
        # 0011
        # 0100
