class Solution:
    def smallestNumber(self, pattern: str) -> str:

        self.smallest = None
        N = len(pattern)

        def backtrack(curr, numStr, index):
            if curr < 1 or curr > 9:
                return None

            if index >= N:
                return numStr

            for i in range(1, 10):
                if str(i) in numStr:
                    continue
    
                if (pattern[index] == "I" and i > curr) or (pattern[index] == "D" and i < curr):
                    ans = backtrack(i, numStr + str(i), index + 1)
                    if ans:
                        return ans
            return None

        for i in range(1,10):
            ans = backtrack(i, str(i), 0)
            if ans:
                return ans

        # Invalid
        return  None