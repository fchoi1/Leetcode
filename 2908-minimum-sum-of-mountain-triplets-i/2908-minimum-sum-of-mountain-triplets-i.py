class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # min and max
        min_left = [nums[0]]
        min_right = [nums[-1]]
        for i in range(1,len(nums)):
            min_left.append(min(min_left[-1], nums[i]))
            min_right.append(min(min_right[-1], nums[-i-1]))
        min_right = min_right[::-1]
        min_sum = float('inf')
        for i in range(1, len(nums)-1):
            if min_left[i] < nums[i] and min_right[i] <  nums[i] :
                min_sum = min(min_sum, min_left[i] + nums[i] + min_right[i])
        return -1 if min_sum == float('inf') else min_sum


