class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        right = max(nums)
        left = 1

        while left < right:
            mid  = (left + right) // 2
            if  sum(math.ceil(x/mid) for x in nums) <= threshold:
                right = mid 
            else:
                left = mid + 1
        return left
        