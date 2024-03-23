class Solution:
    def reverseVowels(self, s: str) -> str:
        res = []
        for char in s:
            if char in "aeiouAEUIOU":
                res.append(char)
        ans = ""
        for char in s:
            if char in "aeiouAEIOU":
                ans += res.pop()
            else:
                ans += char
        return ans