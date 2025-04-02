class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        max_i = 0
        max_d = 0
        ans = max_d * nums[2]

        for n in nums:
            ans = max(ans, max_d * n)
            max_d = max(max_d, max_i - n)
            max_i = max(max_i, n)

        return ans if ans > 0 else 0