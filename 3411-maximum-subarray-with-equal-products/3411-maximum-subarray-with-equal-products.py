class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # 2 loops? start with biggest?

        def prod(arr):
            ans = 1
            for n in arr:
                ans *= n
            return ans
        
        N = len(nums)
        for l in range(N - 1, - 1, -1):
            for i in range(N-l+1):
                curr = nums[i: i + l + 1]
                if prod(curr) == (lcm(*curr) * gcd(*curr)):
                    return len(curr)
        return 0
