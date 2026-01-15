class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash
        def getHash(string):
            t = [0 for _ in range(26)]
            for char in string:
                t[ord(char) - ord('a')] += 1
            return tuple(t)

        anagrams = defaultdict(list)
        for s in strs:
            h = getHash(s)
            anagrams[h].append(s)
        return list(anagrams.values())
