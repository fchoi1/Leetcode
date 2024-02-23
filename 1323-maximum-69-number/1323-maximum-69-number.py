class Solution:
    def maximum69Number (self, num: int) -> int:
        n = ""
        numStr = str(num)
        for i,char in enumerate(numStr):
            if char == '6':
                n += '9'
                break
            else:
                n += char
            

        return int(n + numStr[i+1:])
        