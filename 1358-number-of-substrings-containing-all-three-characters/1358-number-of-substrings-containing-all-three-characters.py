class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        index = {'a':-1, 'b':-1, 'c': -1}
        counts = {'a': 0, 'b': 0, 'c':0 }
        l = count = 0

        for r, char in enumerate(s):
            index[char] = r
            counts[char] += 1

            if counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                count += min(i for i in index.values()) - l + 1

        return count

