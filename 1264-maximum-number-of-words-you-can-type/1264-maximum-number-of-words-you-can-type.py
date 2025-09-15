class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b = set(brokenLetters)
        ans = 0
        for word in text.split(" "):
            for char in word:
                if char in b:
                    break
            else:
                ans += 1
        
        return ans