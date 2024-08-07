class Solution:
    def numberToWords(self, num: int) -> str:
        if not int(num):
            return "Zero"
        
        # 9 digits, every 3 
        step = ["","Thousand", "Million", "Billion"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ones = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        digits = len(str(num))
        numStr = str(num)[::-1]

        def under100(n):
            
            if n > 19:
                if n % 10:
                    return tens[n // 10] + " " + under100(n % 10)
                else:
                    return tens[n // 10] 
            elif n > 10:
                return teens[n-11]
            else:
                return ones[n]

        ans = ""
        for i in range(digits//3 + 1):
            currStr = ""
            for n in numStr[i*3:i*3+3]:
               currStr = n + currStr

            if not currStr:
                break
            curr = int(currStr)
            if not curr:
                continue

            if step[i]:
                ans = " " + step[i] + " " + ans
            
            if curr > 99:
                if curr % 100:
                    ans = ones[curr//100] + " Hundred " + under100(curr % 100) + ans
                else:
                    ans = ones[curr//100] + " Hundred" + ans
            else:
                ans = under100(curr) + ans


        return ans.strip()
