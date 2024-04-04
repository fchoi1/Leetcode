class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a) - 1, len(b) - 1
        carry = 0
        string = ""
        while p1 >= 0 or p2 >= 0:
            val = carry
            if p1 >= 0:
                val += int(a[p1])
                p1 -= 1
  
            if p2 >= 0:
                val += int(b[p2])
                p2 -= 1
            string = str(val % 2) + string
            carry = val > 1

        return "1" + string if carry else string
        