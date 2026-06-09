class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        maxVal = max(nums)
        minVal = min(nums)

        return k * (maxVal - minVal)