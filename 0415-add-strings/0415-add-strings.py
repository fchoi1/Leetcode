class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = n2 = carryOver = 0
        numStr = ""
        while n1 < len(num1) or n2 < len(num2) or carryOver :
            val = carryOver
            if n1 < len(num1):
                val += int(num1[n1])
                n1 += 1
                
            if n2 < len(num2):
                val += int(num2[n2])
                n2 += 1

            carryOver = val // 10
            numStr += str(val % 10)

        return numStr[::-1]

        