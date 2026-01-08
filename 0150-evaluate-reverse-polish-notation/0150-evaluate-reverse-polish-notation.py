class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"

        for n in tokens:
            if n not in ops:
                stack.append(int(n))
            else:
                a = stack.pop()
                b = stack.pop()
                if n == '+':
                    stack.append(b+a)
                elif n == '-':
                    stack.append(b-a)
                elif n == '*':
                    stack.append(b*a)
                elif n == '/':
                    stack.append(int(b/a))

        return stack[-1]