class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # greedy 
        curr = None
        arr = []
        for i, g in enumerate(groups):
            if curr is None:
                curr = g
                arr.append(words[i])
            else:
                if curr != g:
                    arr.append(words[i])
                    curr = g
        return arr