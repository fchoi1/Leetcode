class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        start = 0
        depth = 0

        for i, c in enumerate(s):
            depth += 1 if c == '(' else -1

            if depth == 0:
                ans.append(s[start + 1:i])
                start = i + 1

        return ''.join(ans)