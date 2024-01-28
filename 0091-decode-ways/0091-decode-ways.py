class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [1]
        prev = s[0]
        for char in s[1:]:
            num = int(prev+char)
            if num in [10, 20]:
                if len(dp) == 1:
                    dp.append(1)
                else:
                    dp.append(dp[-2])
            elif char == '0':
                return 0
            elif 0 < num <= 26 and prev != '0':
                if len(dp) == 1:
                    dp.append(2)
                else:
                    dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
            prev = char
        return dp[-1]
