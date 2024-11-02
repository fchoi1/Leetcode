class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split()
        prev = words[0][-1]
        for w in words[1:]:
            if w[0] != prev:
                return False
            prev = w[-1]
        
        return words[0][0] == prev
        