class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        # a b c
        # a + b   = b + c
        # odd == odd
        # even == even
        #

        # odd + even = odd
        # even + odd = odd

        # odd + odd = even
        # even + even = even

        # all odd / all even

        N = len(nums)
        even = sum(i % 2 for i in nums)

        alt = 1
        curr = nums[0] % 2
        for n in nums[1:]:
            if n % 2 != curr:
                curr = n % 2
                alt += 1


        return max(even, N-even, alt)
