class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s = []
        for n in date.split('-'):
            b = bin(int(n))
            s.append(b[2:])
        return "-".join(s)