class Solution:
    def checkRecord(self, s: str) -> bool:
        L = A = 0
        for char in s:
            if char == 'A':
                A += 1
                if A >= 2:
                    return False
            if char == 'L':
                L += 1
                if L >= 3:
                    return False
            else:
                L = 0
        return True
        