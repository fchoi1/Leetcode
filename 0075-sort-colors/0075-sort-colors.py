class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        zero = counts[0]
        one = counts[1]

        for i in range(zero):
            nums[i] = 0
        for i in range(zero, zero+one):
            nums[i] = 1
        for i in range(zero+one, len(nums)):
            nums[i] = 2

        