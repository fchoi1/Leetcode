class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        minAvg = inf

        nums.sort()

        for i in range(len(nums)//2):
            minAvg = min(minAvg, (nums[i] + nums[-i-1])/2)
        return minAvg