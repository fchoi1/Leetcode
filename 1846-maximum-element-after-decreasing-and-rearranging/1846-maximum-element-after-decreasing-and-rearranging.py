class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        curr = 0
        for i,n in enumerate(arr):
            curr = min(curr + 1, n)
            ans = max(ans, curr)

        return ans