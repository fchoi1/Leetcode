class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i, n in enumerate(nums):
            if index < i:
                index = i
            # print(i, index, nums)
            while nums[index] == 0:
                index += 1
                if index == len(nums):
                    return
            # print('after',nums[index], index, nums)
            if n == 0:
                nums[i], nums[index] = nums[index],0

        