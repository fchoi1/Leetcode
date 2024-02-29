class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = left = 0
        product = 1
        for i,n in enumerate(nums):
            product *= n
            while left < i and product >= k:
                product /= nums[left]
                left += 1
            if product < k:
                count += i - left + 1
        return count
