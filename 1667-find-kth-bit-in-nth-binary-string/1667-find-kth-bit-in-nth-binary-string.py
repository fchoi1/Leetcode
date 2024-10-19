class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(binStr):
            new = ""
            for b in binStr[::-1]:
                if b == '0':
                    new += '1'
                else:
                    new += '0'
            return new

        length = 2 ** n + 1
        index = int(math.sqrt(k))
        string = "0"
        while len(string) < k:
            string += "1" + invert(string)
        return string[k-1]

        