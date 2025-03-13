class Solution:
    def finalString(self, s: str) -> str:
        curr = ''

        for char in s:
            if char == 'i':
                curr = curr[::-1]
                continue
            curr += char
        return curr