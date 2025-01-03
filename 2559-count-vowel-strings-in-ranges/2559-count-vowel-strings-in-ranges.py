class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowels = 'aeiou'
        count = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                count += 1
            prefix.append(count)
        ans = []
        for s,e in queries:
            ans.append(prefix[e + 1] - prefix[s])
        return ans