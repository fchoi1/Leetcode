class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        closed = s.count(')')
        ans = ""
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
                closed -= 1
            if count < 0:
                count = 0
                continue
            if count > closed:
                count = closed
                continue
            ans += char
        return ans

        # if count is neg, dont include brackeet
        # keep track of positive


        # (((a). -> ((

        # ))) (((
        