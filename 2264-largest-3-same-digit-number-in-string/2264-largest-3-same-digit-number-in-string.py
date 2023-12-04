class Solution:
    def largestGoodInteger(self, num: str) -> str:
        total = None
        for i,c in enumerate(num[:-2]):
            print(i, c, num[i:i+3])
            if all(x == c for x in num[i:i+3]) and num[i:i+3].isdigit():
                if total == None:
                    total = int(num[i:i+3])
                else:
                    total = max(total, int(num[i:i+3]))
        if total == 0:
            return "000"
        return str(total) if total != None else ""