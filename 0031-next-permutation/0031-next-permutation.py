class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1 2 3 
        # 1 3 2


        # go for the end until descending, switch end
        # 


        # 3 2 1 -> needs full reverse

        # 3 1 4 2 -> go until 2 > 1, no need to reverse? we do?
        # 3 2 1 4


        # 3 1 5 4 2

        # 3 2 1 4 5

        # 3 1 4 5 2
        # 3 1 5 2 4

        N = len(nums) - 1
        swap = -1
        for i in range(N, 0, -1):
            if nums[i - 1] < nums[i]:
                # found the switch 
                swap1 = i - 1
                break
        else:
            nums.reverse()
            return
            
        for i in range(N, swap1, -1):
            if nums[swap1] < nums[i]:
                swap2 = i
                break
        else:
            print("Logic error?")

        nums[swap1], nums[swap2] = nums[swap2], nums[swap1]
        print("Swap", swap1, swap2, nums,  nums[swap1::-1])

        nums[swap1+1:] = nums[swap1+1:][::-1]
        print(nums)