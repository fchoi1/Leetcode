class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for n in num:
            while arr and k > 0 and n < arr[-1]:
                arr.pop()
                k -= 1
            if not arr and n == '0':
                continue
            arr.append(n)
            if k == -1:
                break
        
        while k > 0 and arr:
            arr.pop()
            k -= 1
        
        digitStr = ""
        for n in arr:
            digitStr += str(n)
        return digitStr if digitStr else '0'
