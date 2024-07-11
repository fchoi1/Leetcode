class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack
        words = []
        word = ''
        for char in s:
            if char == '(':
                words.append(word)
                word = ''
            elif char == ')':
                # pop
                word = word[::-1]
                word = words.pop() + word
            else:
                word += char
        return word