class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = defaultdict(int)
        ans = [None] * 26
        for char in word:
            key = ord(char.lower()) - ord('a')
            c[char] += 1

            if ans[key] is None:
                if c[char.upper()] > 0 and c[char.lower()] > 0:
                    ans[key] = True

            if char.lower() == char:
                if c[char.upper()] > 0:
                    ans[key] = False

        
        return sum(v if v else 0 for v in ans)

