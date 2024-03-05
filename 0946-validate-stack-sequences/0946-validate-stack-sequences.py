class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop = 0
        stack = []

        for val in pushed:
            stack.append(val)
            while stack and popped[pop] == stack[-1]:
                stack.pop()
                pop += 1

        return len(stack) == 0