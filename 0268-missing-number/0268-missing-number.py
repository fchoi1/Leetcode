class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            n = nums[i]

            if i == n or n > len(nums):
                continue

            while n <len(nums) and  n != nums[n]:
                temp = nums[n]
                nums[n] = n
                n = temp
            if n >= len(nums):
                nums[i] = n
        for i,n in enumerate(nums):
            if i != n:
                return i
        return len(nums) 
        

        