class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        i = 1
        count = curr = 0
        while i <= n:
            if i not in banned:
                curr += i
                count += 1
            if curr > maxSum:
                return count - 1
            i += 1

        return count