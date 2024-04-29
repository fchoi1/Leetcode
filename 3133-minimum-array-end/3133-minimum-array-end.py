class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        nStr = str(bin(n-1))[2:][::-1]
        xStr = str(bin(x))[2:][::-1]
        binString = ""
        i = j = 0
        while i < len(nStr) or j < len(xStr):
            if j < len(xStr):
                j += 1
                if xStr[j-1] == '1' or i >= len(nStr):
                    binString = xStr[j-1] + binString
                    continue
            if i < len(nStr):
                binString = nStr[i] + binString
                i += 1

        # 100
        # 101
        return int(binString,2)
