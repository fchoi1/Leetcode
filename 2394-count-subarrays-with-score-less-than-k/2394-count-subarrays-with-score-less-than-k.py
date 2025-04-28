class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        
        N = len(nums)
        total = N * (N+1)//2
        l = c = curr = 0

        for r, n in enumerate(nums):
            curr += n
            while curr * (r - l + 1) >= k:
                c += N - r
                curr -= nums[l]
                l += 1     
        return total - c

        