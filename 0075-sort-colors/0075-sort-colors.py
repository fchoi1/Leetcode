class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        zeros = counts[0]
        ones = counts[1]
        twos = counts[2]

        nums[:zeros] = [0] * zeros
        nums[zeros:zeros+ones] = [1] * ones
        nums[zeros+ones:] = [2] * twos

        # 2 0 2 1 1 0
        # 0 2 2 1 1 0
        # 0 0 2 2 1 0