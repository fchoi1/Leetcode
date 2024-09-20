class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        # find the most common,
        # center
        slow = 1

        N = len(s)
        longest = 0
        while slow < N // 2 + 1:
            # print('even',s[:slow], s[slow:slow*2][::-1])
            # print('odd', s[:slow],s[slow-1:slow*2-1][::-1])
            if s[:slow] == s[slow-1:slow*2-1][::-1]:
                longest = slow * 2 - 1
            if s[:slow] == s[slow:slow  * 2][::-1]:
                longest = slow * 2
            slow += 1
        return  s[longest:][::-1] + s
        