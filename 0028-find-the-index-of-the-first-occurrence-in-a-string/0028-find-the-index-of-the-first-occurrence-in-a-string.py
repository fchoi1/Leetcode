class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle)
        while end <= len(haystack):
            print(needle, haystack[start:end])
            if needle == haystack[start:end]:
                return start
            start += 1
            end += 1
        return -1