class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort() 
        target1 = nums[len(nums)//2]
        moves1 = 0
        for n in nums:
            moves1 += abs(n - target1)
        return moves1