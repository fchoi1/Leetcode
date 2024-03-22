class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
        # minVal = min(nums)
        # moves = 0
        # for n in nums:
        #     moves += n - minVal
        # return moves
