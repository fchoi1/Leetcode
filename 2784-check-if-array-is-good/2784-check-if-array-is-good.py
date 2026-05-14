class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N = len(nums) - 1
        c = defaultdict(int)
        curr = 0

        for n in nums:
            c[n] += 1
            curr += n
            
        return len(c) == N and c[N] == 2 and curr == N * (N + 1) // 2 + N