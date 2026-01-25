class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0

        # sort
        nums.sort()
        minDiff = inf
        N = len(nums)

        print(nums)
        for i in range(N - k  + 1):
            print(i, i + k - 1 , nums[i + k - 1 ] , nums[i])
            minDiff = min(minDiff, nums[i + k - 1 ] - nums[i])


        return minDiff