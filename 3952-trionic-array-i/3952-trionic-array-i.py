class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # up down up

        if len(nums) == 3 or nums[1] < nums[0]:
            return False

        switch = 0
        increase = True

        for prev, curr in zip(nums, nums[1:]):
            if prev == curr:
                return False
            
            if increase and curr < prev:
                increase = False
                switch += 1
            elif not increase and curr > prev:
                increase = True
                switch += 1
            
            print(increase, prev, curr, switch)
            
        print(switch, increase)
        return switch == 2