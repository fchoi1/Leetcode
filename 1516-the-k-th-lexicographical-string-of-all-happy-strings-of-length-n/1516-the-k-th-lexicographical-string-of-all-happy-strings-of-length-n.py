class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

        self.ans = ""
        self.count = 0

        # generate happy strings
        def backtrack(s):
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.ans = s
                    return True
                return False

            for char in "abc":
                if s and s[-1] == char:
                    continue
                if backtrack(s + char):
                    return True
            return False
        
        backtrack("")
        return self.ans