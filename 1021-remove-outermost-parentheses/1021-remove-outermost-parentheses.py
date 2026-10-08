class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""

        count = 0

        for b in s:

            if b == '(':
                count += 1
                
                if count > 1:
                    ans += b
            else:
                count -= 1
        
                if count > 0:
                    ans += b
            

        return ans