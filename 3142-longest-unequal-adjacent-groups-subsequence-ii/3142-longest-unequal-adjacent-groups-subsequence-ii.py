class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # hamming dist
        w_dict = dict(zip(words, groups))
        one_away = defaultdict(set)
        dp = {} # word: ([], group)
        ans = []
        for w, g in zip(words, groups):
            dp[w] = ([w], g)
            for i,char in enumerate(w):
                curr = list(w)  
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == char:
                        continue
                    curr[i] = c
                    one = "".join(curr)
                    if one in dp:
                        arr, group = dp[one]
                        if group != g:
                            if w not in dp or (w in dp and len(arr) + 1 > len(dp[w][0])):
                                dp[w] = (arr + [w], g)
            if len(dp[w][0]) > len(ans):
                ans = dp[w][0]
            
            
        return ans