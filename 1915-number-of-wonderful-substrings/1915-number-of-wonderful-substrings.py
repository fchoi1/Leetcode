class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        seen = defaultdict(int)
        val = 0
        wonderful = 0
        seen[val] += 1
        for char in word:
            val ^= 1 << (ord(char)-ord('a'))
            wonderful += seen[val]
            for n in range(10):
                oneOff = val ^ (1 << n)
                if oneOff in seen:
                    wonderful += seen[oneOff]
            seen[val] += 1
        return wonderful