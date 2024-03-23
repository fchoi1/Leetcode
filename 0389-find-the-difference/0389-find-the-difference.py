class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)

        for char in tCount:
            if char not in sCount or sCount[char] != tCount[char]:
                return char
        return None
        