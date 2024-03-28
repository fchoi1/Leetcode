class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        slow = 0 
        count = defaultdict(int)
        longest = 1
        for i, n in enumerate(nums):
            count[n] += 1
            while slow <= i and count[n] > k:
                count[n] -= 1
                slow += 1
            longest = max(longest, i - slow + 1)
        return longest