class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = avg = sum(nums[:k])/k

        for i in range(len(nums)-k):
            avg = (avg * k - nums[i] + nums[i + k]) / k
            maxAvg = max(maxAvg, avg)
            
        return maxAvg