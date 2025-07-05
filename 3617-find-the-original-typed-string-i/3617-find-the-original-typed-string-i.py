class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                total += 1
        return total
