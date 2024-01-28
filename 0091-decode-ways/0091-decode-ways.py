class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0" or "00" in s:
            return 0
        if len(s) == 1:
            return 1

        dp = [1]
        if s[1] == '0' and s[0] not in '12':
            return 0
        elif s[1] == '0' and s[0] in '12' or not 0 < int(s[:2]) <= 26 :
            dp.append(1)
        else:
            dp.append(2)

        prev = s[1]
        for char in s[2:]:
            num = int(prev+char)
            if char == '0':
                if prev in '12':
                    dp.append(dp[-2])
                else:
                    return 0
                prev = char
                continue
            if 0 < num <= 26 and prev != '0':
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
            prev = char
        return dp[-1]
# 26110
# 2 6 1 10
# 26 1 10
