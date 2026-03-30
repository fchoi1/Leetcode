class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # swaps?
        N = len(s1)
        swaps1 = [defaultdict(int), defaultdict(int)]
        swaps2 = [defaultdict(int), defaultdict(int)]

        for i in range(N):
            swaps1[i % 2][s1[i]] += 1
            swaps2[i % 2][s2[i]] += 1



        for i, (c1, c2) in enumerate(zip(s1, s2)):

            idx = i % 2

            if c1 == c2 and swaps1[idx][c1] > 0 and swaps2[idx][c2] > 0:
                swaps1[idx][c1] -= 1
                swaps2[idx][c2] -= 1
            # valid swap s1
            elif c2 in swaps1[idx] and swaps1[idx][c2] > 0 and swaps2[idx][c2] > 0:
                swaps1[idx][c2] -= 1
                swaps2[idx][c2] -= 1
            elif c1 in swaps2[idx] and swaps2[idx][c1] > 0 and swaps1[idx][c1] > 0:
                swaps1[idx][c1] -= 1
                swaps2[idx][c1] -= 1
            else:
                return False

        return True