class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counts = Counter(s)
        prevCount = defaultdict(int)
        seen = set()
        for char in s:
            for letter in ascii_lowercase:
                nextCount = counts[letter] if letter != char else counts[letter] - 1
                if prevCount[letter] > 0 and nextCount - prevCount[letter] > 0:
                    seen.add((letter, char))
            prevCount[char] += 1
        return len(seen)
