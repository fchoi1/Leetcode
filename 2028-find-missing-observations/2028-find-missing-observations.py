class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        missing = total * mean - sum(rolls)

        times = missing / n
        if times < 1 or times > 6:
            return []
        times = int(times)
        diff = missing - times * n

        if diff > 0:
            affected = diff // (6-times)
            remain = diff - affected * (6 - times)
            if remain:
                return [times + min(diff, 6-times) for _ in range(affected)] + [times for _ in range(n-affected-1)] + [times + remain]
            return [times + min(diff, 6-times) for _ in range(affected)] + [times for _ in range(n-affected)]
        return [times for _ in range(n)]

        
