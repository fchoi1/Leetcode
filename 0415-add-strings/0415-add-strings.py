class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1 = num1[::-1]
        num2 = num2[::-1]

        carry =  i = j = 0
        ans = ""
        while i < len(num1) or j < len(num2):
            
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if j < len(num2) else 0
            total = n1 + n2 + carry
            val = (total) % 10 
            carry = (total) // 10

            ans = str(val) + ans
            i += 1
            j += 1


        if carry:
            ans = "1" + ans
            
        return ans