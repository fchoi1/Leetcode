class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = inf

        for n in nums:
            curr = 0
            for char in str(n):
                curr += int(char)
            
            ans = min(ans,curr)
        return ans