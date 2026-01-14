class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[left] = nums[i]
                if left != i:
                    nums[i] = 0
                left += 1
