class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort() 
        target1 = nums[len(nums)//2]
        target2 = nums[len(nums)//2-1]
        moves1 = moves2 = 0
        for n in nums:
            moves1 += abs(n - target1)
            moves2 += abs(n - target2)
        return min(moves1, moves2)

        # we need to know mean 

        # 37/ 10 = 3.7

        # 1 1 1 3 3 3 5 5 5 10
        # 0 0 0 2 2 2 4 4 4 9 = 27
        # 1 1 1 1 1 1 3 3 3 8 = 23
        # 2 2 2 0 0 0 2 2 2 7 = 19
        # 3 3 3 1 1 1 1 1 1 6 = 21
        # 4 4 4 2 2 2 0 0 0 5 = 23

        # something with the counts 
        # mean?

        # 1 2 3 4 5 6
        # 2 1 0 1 2 3 = 9
        # 3 2 1 0 1 2 = 9

        #  1 1 1 3 3 7
        #  0 0 0 2 2 6 = 10
        #  1 1 1 1 1 5 = 10
        #  2 2 2 0 0 3 = 10
        #  3 3 3 1 1 3 = 14

        #  1 1 1 5 10 
        # 5 + 0 + 4 + 4 + 4 = 17
        # 6 + 1 + 3 + 3 + 3 = 16
        # 7 + 2 + 2 + 2 + 2 = 15
        # 8 + 3 + 1 + 1 + 1 = 14
        # 9 + 4 + 0 + 0 + 0 = 13


        # 1 2 3 

        # 2 + 1 + 0 = 3
        # 1   0   1 = 2
        # 0   1   2 = 3

        # 1 2 4 5
        # 4 3 1 0 = 8
        # 3 2 0 1 = 6
        # 2 1 1 2 = 6 
        # 1 0 2 3 = 6
        # 0 1 3 4 = 8
        return 1