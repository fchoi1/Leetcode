class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        index = defaultdict(int)
        counts = defaultdict(int)
        l = count = 0
        for r, char in enumerate(s):
            index[char] = r
            counts[char] += 1
            
            if counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                count += min(i for i in index.values()) - l + 1

        return count

