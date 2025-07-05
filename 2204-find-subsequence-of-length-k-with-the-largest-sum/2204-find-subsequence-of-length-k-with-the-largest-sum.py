class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = []

        for i,n in enumerate(nums):
            heappush(h, (n,i))
            if len(h) > k:
                heappop(h)

        return [x[0] for x in sorted(h, key=lambda x:x[1])]