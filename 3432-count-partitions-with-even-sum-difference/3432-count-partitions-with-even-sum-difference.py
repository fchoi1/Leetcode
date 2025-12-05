class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        total = sum(nums)
        parts = 0
        curr = 0
        for n in nums[:-1]:
            curr += n
            if ((total - curr) - curr) % 2 == 0:
                parts += 1
        
        return parts