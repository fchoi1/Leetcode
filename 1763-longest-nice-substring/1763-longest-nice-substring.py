class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def getMissing(s):
            miss = set()
            seen = set()

            for char in s:
                seen.add(char)
                if (char == char.upper() and char.lower() in seen) or (char == char.lower() and char.upper() in seen):
                    miss.discard(char.upper())
                    miss.discard(char.lower())
                else:
                    miss.add(char)
            return miss
        # aaaZAAA
        def checkNice(s):
            missing = getMissing(s)
            if len(getMissing(s)) == 0 or not s:
                return s
            for i,char in enumerate(s):
                if char in missing:
                    left = checkNice(s[:i])
                    right = checkNice(s[i+1:])
                    return left if len(left) >= len(right) else right
        
        return checkNice(s)
        

        # YaAaaazy
        