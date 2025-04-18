class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):

            prev = s[0]
            new = ''
            count = 1
            for char in s[1:]:
                if char == prev:
                    count += 1
                else:
                    new += f'{str(count)}{prev}'
                    count = 1
                prev = char
            new += f'{str(count)}{prev}'
            s = new
        return s
        