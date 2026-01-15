class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 end 
        # 0 start
        zeroes = 0

        c = Counter(nums)
        print(c)
        for i in range(c[0]):
            nums[i] = 0
        
        for i in range(c[0], c[0] + c[1]):
            nums[i] = 1
        
        for i in range(c[0] + c[1], len(nums)):
            nums[i] = 2