class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        for i,n in enumerate(nums):
            res.append(nums[(i + n) % N])
        return res