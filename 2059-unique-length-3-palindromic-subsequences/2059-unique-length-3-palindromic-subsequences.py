class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pali = set()

        # just need counts of dupes and in between>
        counts = Counter(s)
        print(counts)


        pali = 0

        for char, c in counts.items():

            if c < 2:
                continue
            start = s.index(char)
            end = len(s) - s[::-1].index(char)
            unique = set(s[start+1:end-1])
            pali += len(unique)
        return pali