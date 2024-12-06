class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        curSum = 0

        for num in range(1, n + 1):
            if num in banned:
                continue

            if curSum + num > maxSum:
                return count
            else:
                count += 1
                curSum += num
        return count