class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        maxLen = 0
        N = len(nums)
        for i in range(N):
            even = set()
            odd = set()
            for j in range(i, N):
                if nums[j] % 2 == 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                
                if len(odd) == len(even):
                    maxLen = max(maxLen, j - i + 1) 
                
        
        return maxLen