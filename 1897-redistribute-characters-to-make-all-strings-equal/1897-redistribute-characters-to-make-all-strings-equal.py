class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0] * 26
        for word in words:
            for char in word:
                count[ord(char)-ord('a')] += 1
        for n in count:
            if n % len(words) != 0:
                return False
        return True