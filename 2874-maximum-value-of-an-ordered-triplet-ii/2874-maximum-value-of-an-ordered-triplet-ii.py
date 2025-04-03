class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_d = ans = max_i = 0

        for n in nums:
            ans = max(ans, max_d * n)      
            max_d = max(max_d, max_i - n)   
            max_i = max(max_i, n)           

        return ans
        