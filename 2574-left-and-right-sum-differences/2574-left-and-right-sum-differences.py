class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l = r = 0
        s = sum(nums)
        ans = []
        for i in range(N):
            r += nums[i]
            rs = s - r
            ans.append(abs(rs - l))
            l += nums[i]

        return ans