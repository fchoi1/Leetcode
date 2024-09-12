class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        count = 0
        for word in words:
            for c in word:
                if c not in a:
                    break
            else:
                count += 1
        return count