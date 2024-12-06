class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        count = curr = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            curr += i
            count += 1
            if curr > maxSum:
                return count - 1
        return count

