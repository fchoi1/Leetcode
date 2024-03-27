class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        slow = count = 0
        product = 1
        for i,n in enumerate(nums):
            product *= n
            while slow <= i and product >= k:
                count += i - slow
                product /= nums[slow]
                slow += 1
        count += (i-slow+1) * (i-slow+2) / 2
        return int(count)