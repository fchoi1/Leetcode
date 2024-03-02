class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))
        return [x*x for x in nums]
        