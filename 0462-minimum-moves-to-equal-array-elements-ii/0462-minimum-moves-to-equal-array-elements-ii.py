class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort() 
        target1 = nums[len(nums)//2]
        target2 = nums[len(nums)//2-1]
        moves1 = moves2 = 0
        for n in nums:
            moves1 += abs(n - target1)
            moves2 += abs(n - target2)
        return min(moves1, moves2)