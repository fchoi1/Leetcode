class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minVal = min(nums)
        moves = 0
        for n in nums:
            moves += n - minVal
        return moves
