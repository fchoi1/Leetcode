class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(n % 3, 3 - n % 3) for n in nums)