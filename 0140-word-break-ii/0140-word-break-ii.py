class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def getSubsets(index, currStr):
            if index >= len(s):
                res.append(currStr.strip())
                return
  
            for word in wordDict:
                if s[index:].startswith(word):
                    getSubsets(index + len(word), currStr + word + " ")
                    

        getSubsets(0, "")
        return res
        