class Solution:
    def countAndSay(self, n: int) -> str:
        string = "1"
        for _ in range(n-1):
            new = ""
            count = 1
            prev = string[0]
            for c in string[1:]:
                if prev == c:
                    count += 1
                else:
                    new += str(count) + prev
                    count = 1
                prev = c
            new  += str(count) + prev
            string = new
        return string