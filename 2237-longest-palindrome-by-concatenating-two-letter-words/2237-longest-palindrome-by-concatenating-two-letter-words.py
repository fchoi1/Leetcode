class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = defaultdict(int)

        for w in words:
            pairs[tuple(w)] += 1

        length = 0
        double = 0
        for p in pairs:
            times = 0
            if p[0] == p[1]:
                times = pairs[p] // 2 * 2
                if not double:
                    double = pairs[p] % 2 * 2
            elif p[0] != p[1] and (p[1], p[0]) in pairs:
                times = min(pairs[p], pairs[(p[1], p[0])])
            length += times * 2
        return length + double