class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for n in num:
            while arr and k > 0 and n < arr[-1]:
                arr.pop()
                k -= 1
            arr.append(n)
            if k == -1:
                break
        
        while k > 0 and arr:
            arr.pop()
            k -= 1
        
        digitStr = ""
        leading = True
        for n in arr:
            if leading and n == '0':
                continue
            else:
                leading = False
            digitStr += str(n)
        return digitStr if not leading else '0'
