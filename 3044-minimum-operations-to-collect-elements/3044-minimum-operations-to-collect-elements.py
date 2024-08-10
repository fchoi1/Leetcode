class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = k * (k+1) // 2
        curr = 0
        seen = set()
        nums.reverse()
        for i, n in enumerate(nums):
            if n in seen or not 1 <= n <= k:
                continue
            curr += n
            seen.add(n)
            if curr == target:
                return i + 1
        return -1

