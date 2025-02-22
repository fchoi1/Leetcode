class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        inc = 0
        minVal = smallest = inf

        for prev, curr in zip(nums, nums[1:]):
            if curr > minVal:
                return True
            if curr > prev or curr > smallest:
                minVal = min(minVal, curr)
            smallest = min(prev, smallest)

        return False
        