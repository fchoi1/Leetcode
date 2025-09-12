class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # conditions

        # need end to find next?


        #  5 1 (4 3) 2
        #  5 1 4  2 3
        #  5 1 2 4 3
        #  5 2 1 4 3


        #  5 3 6 7 2

        # 5 3 7 2 6


        #  5 3 9 7 2
        #  5 7 2 3 9

        #  5 3 9 7 3
        #  5 7 3 3 9

        #  5 2 1 3 4


        #  1 3 5 4
        #  1 4 3 5
        def reverse(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # get the index to swap with last when non acendubg'

        index = len(nums) - 1

        while index - 1 >= 0 and nums[index - 1] >= nums[index]:
            index -= 1
        index -= 1
        if index == -1:
            reverse(0)
            return

        # get the next smallest node
        next_largest = len(nums) - 1
        while next_largest - 1 >- 0 and nums[index] >= nums[next_largest]:
            next_largest -= 1
        nums[index], nums[next_largest] = nums[next_largest], nums[index]
        reverse(index + 1)





        # 2 3 1 
        # 3 1 2

        # 3 1 2 1
        # 3 2 1 1

        # 4 2 3 1
        # 