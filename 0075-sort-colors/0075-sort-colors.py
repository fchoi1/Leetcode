class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = Counter(nums)
        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1
        for i in range(counts[1] + counts[0], len(nums)):
            nums[i] = 2
