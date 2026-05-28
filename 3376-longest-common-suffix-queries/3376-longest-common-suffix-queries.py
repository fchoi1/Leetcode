class Trie:
    def __init__(self, char, index = -1):
        self.val = char
        self.length = inf
        self.index = index
        self.next = {}

    def updateWord(self, newWord, index):
        N = len(newWord)
        if N < self.length:
            self.length = N
            self.index = index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # create a trie or nested dict

        root = Trie(None)

        for i,word in enumerate(wordsContainer):
            curr = root
            curr.updateWord(word, i)
            for char in word[::-1]:
                if char not in curr.next:
                    curr.next[char] = Trie(char, word)

                curr = curr.next[char]
                curr.updateWord(word, i)
        

        ans = []
        for word in wordsQuery:
            curr = root
            for char in word[::-1]:
                if char not in curr.next:
                    break
                curr = curr.next[char]
            ans.append(curr.index)
        return ans
                
                


        