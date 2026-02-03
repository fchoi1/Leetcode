class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        # impossible if lenghth is 3 or starts off decreasing
        if len(nums) <= 3 or nums[1] < nums[0]:
            return False

        switch, increase = 0, True

        for prev, curr in zip(nums, nums[1:]):
            # Can't be equal
            if prev == curr:
                return False
            
            # count how many times it switches
            if increase != (curr > prev):
                increase = not increase
                switch += 1

        return switch == 2