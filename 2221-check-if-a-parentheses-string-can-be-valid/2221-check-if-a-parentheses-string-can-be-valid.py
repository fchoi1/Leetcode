class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        def checkStr(s,locked, reverse=False):
            free = 0
            curr = 0
            bracket = "(" if not reverse else ")"
            for b, l in zip(s, locked):
                if l == '0':                    
                    free += 1
                else:
                    curr += 1 if b == bracket else -1
                    
                    if curr < 0:
                        if not free:
                            return False
                        free -= 1
                        curr = 0
            return True
        # check forward and backward
        return checkStr(s,locked) and checkStr(s[::-1], locked[::-1], True)
           
        