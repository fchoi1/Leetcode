class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        def checkStr(s,locked):
            free = 0
            curr = 0

            for b, l in zip(s, locked):
                if l == '0':                    
                    free += 1
                else:
                    curr += 1 if b == '(' else -1
                    
                    if curr < 0:
                        if not free:
                            return False
                        free -= 1
                        curr = 0
            return True
        return checkStr(s,locked) and checkStr(['(' if b == ')' else ')' for b in s][::-1], locked[::-1])
           
        