class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        # low
        # 1 000 000 000 
        minDigits = len(str(low))
        maxDigits = len(str(high))
        string = '123456789'
        ans = []
        for digits in range(minDigits, maxDigits + 1):
            for n in range(0, 9):
                if n + digits > 9:
                    break
                strNum = string[n: n + digits]
                if low <= int(strNum) <= high:
                    ans.append(int(strNum))
    
        return ans