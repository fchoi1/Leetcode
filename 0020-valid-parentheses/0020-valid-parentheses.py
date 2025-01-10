class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = '({['
        c = ')}]'
        b_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for b in s:
            if b in o:
                stack.append(b_map[b])
                continue
            if not stack or b != stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0