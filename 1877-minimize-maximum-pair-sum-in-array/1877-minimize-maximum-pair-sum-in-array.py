class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # max and min
        # bucket sort????

        # 1 2  4 100

        print(sorted(nums))
        # 
        N = len(nums)
        l = 0
        r = N - 1
        maxVal = -inf
        nums.sort()
        while l < r:
            maxVal = max(maxVal, nums[r] + nums[l])
            l += 1
            r -= 1


        return maxVal