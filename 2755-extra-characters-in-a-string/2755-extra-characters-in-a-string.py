class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self,word):
        head = self
        for letter in word:
            if letter in head.children:
                head = head.children[letter]
            else:
                head.children[letter] = Trie()
                head = head.children[letter]
        head.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie_head = Trie()
        #Create Trie
        for word in dictionary:
            trie_head.insert(word)
        # trie_head.printTrie()
        dp = [None for _ in range(len(s)+1)]
        dp[-1] = 0

        for start in range(len(s)-1,-1, -1):
            dp[start] = dp[start+1]+1
            node = trie_head
            for end in range(start,len(s)):
                if s[end] not in node.children:
                    break
                node  = node.children[s[end]]
                if node.isEnd:
                    dp[start] = min(dp[start],dp[end+1])
        return dp[0]

        