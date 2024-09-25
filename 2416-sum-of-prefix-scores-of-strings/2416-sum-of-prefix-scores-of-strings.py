class Trie:
    def __init__(self, value=None):
        self.end = 0
        self.value = value
        self.children = {}


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Trie(char)
                curr = curr.children[char]
                curr.end += 1
        
        score = []
        for word in words:
            curr = root
            currScore = 0
            for char in word:
                if char not in curr.children:
                    break
                curr = curr.children[char]
                currScore += curr.end
            score.append(currScore)
    
        return score
        