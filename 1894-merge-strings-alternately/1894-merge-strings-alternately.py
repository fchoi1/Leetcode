from collections import deque

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr =  ''

        w1 =  deque(word1)
        w2 =  deque(word2)
        while w1 and w2:
            newStr += w1.popleft() + w2.popleft()

        newStr += "".join(w1) + "".join(w2)
        return newStr

        