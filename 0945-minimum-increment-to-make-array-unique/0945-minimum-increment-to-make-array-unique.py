class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        curr = float("-inf")
        for n in nums:
            if n <= curr:
                curr += 1
                moves += (curr - n)
            else:
                curr = n
        return moves
        