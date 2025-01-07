class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ans = []
        for w in words:
            for word in words:
                if w != word and w in word:
                    ans.append(w)
                    break
        return ans