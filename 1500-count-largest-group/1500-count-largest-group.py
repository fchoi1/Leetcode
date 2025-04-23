class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 999

        counts = defaultdict(int)
        

        for i in range(1, n+1):
            counts[sum(int(x) for x in str(i))] += 1

        max_count = max(counts.values())
        return sum(c == max_count for c in counts.values())
