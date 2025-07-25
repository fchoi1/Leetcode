class Solution:
    def maxSum(self, nums: List[int]) -> int:
        highest = max(nums)
        if highest <= 0:
            return highest
        

        return sum(set([n if n > 0 else 0 for n in nums]))
        