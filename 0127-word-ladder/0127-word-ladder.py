class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
        q = [beginWord]
        seen = set()
        step = 0
        while q:
            tempQ = []
            for word in q:
                if word == endWord:
                    return step + 1
                if word in seen:
                    continue
                seen.add(word)
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        temp = word[:i] + c + word[i+1:]
                        if temp in wordSet:
                            tempQ.append(temp)
            q = tempQ
            step += 1
        return 0
        