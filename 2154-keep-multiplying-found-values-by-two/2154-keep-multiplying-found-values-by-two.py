class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n_set = set(nums)

        while original in n_set:
            original *= 2
        return original 