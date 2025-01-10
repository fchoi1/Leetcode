class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash
        d = defaultdict(list)
        ans = []
        for word in strs:
            t = [0] * 26
            for char in word:
                t[ord(char)-ord('a')] += 1
            d[",".join(str(n) for n in t)].append(word)
        
        return [v for v in d.values()]
            