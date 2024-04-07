class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        o_bracket = 0 # checking for when closed > open
        c_bracket = 0 # checking after of when closed == open
        for char in s:
            if char == "(":
                c_bracket += 1
                o_bracket += 1
            elif char == ")":
                o_bracket -= 1
                c_bracket = max(0, c_bracket - 1)
            else:
                o_bracket += 1
                c_bracket = max(0, c_bracket - 1) # counts as something to close the closed bracket

            if o_bracket < 0:
                return False
        return c_bracket == 0
        