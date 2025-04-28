class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # prefix sum
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        
        N = len(nums)
        total = N * (N+1)//2
        l = c = 0

        print("PRE", prefix)
        for r, n in enumerate(nums):
            score = (prefix[r + 1] - prefix[l]) * (r - l + 1)
            while score >= k:
                c += N - r
                l += 1
                score = (prefix[r + 1] - prefix[l]) * (r - l + 1)
     
        return total - c

        