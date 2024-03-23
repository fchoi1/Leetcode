class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        index = 0
        for i, char in enumerate(columnTitle[::-1]):
            index += 26 ** i  * (ord(char) - ord("A") + 1)
        return index
        