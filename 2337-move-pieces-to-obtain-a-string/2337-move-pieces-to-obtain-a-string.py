class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left = right = 0
        for s,t in zip(start, target):
       
            if s == 'R':
                right += 1     
            if t == "L":
                left += 1

            if s == 'L':
                if left == 0 or right > 0:
                    return False
                left -= 1
            if t == "R":
                if right == 0 or left > 0:
                    return False
                right -= 1
            
       
        return left == 0 and right == 0
        