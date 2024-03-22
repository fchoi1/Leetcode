class Solution:
    def minMoves(self, nums: List[int]) -> int:

        sortedNums = sorted(nums, reverse=True)
        moves = 0
        minVal = sortedNums[-1]
        print(sortedNums)
        for n in sortedNums[:-1]:
            moves += n - minVal
        return moves
