class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        swaps1 = [defaultdict(int), defaultdict(int)]
        swaps2 = [defaultdict(int), defaultdict(int)]

        for i in range(len(s1)):
            swaps1[i % 2][s1[i]] += 1
            swaps2[i % 2][s2[i]] += 1

        return swaps1 == swaps2