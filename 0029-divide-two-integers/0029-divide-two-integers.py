class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = abs(dividend)
        a = abs(divisor)

        if divisor == 1:
            return max(min(dividend, 2**31-1),-2**31 )
        elif divisor == -1:
            return max(min(-dividend, 2**31-1),-2**31 )

        times = [(a, 1)]
        while n > 0:
            val, t = times[-1]
            times.append((val+val, t+t))
            n -= (val + val)
            print(n, val)
        print(times)
        ans = 0
        n = abs(dividend)
        while times:
            if n - times[-1][0] >= 0:
                ans += times[-1][1]
                n -= times[-1][0]
            times.pop()
        return ans if (dividend < 0 and divisor < 0) or (divisor > 0 and dividend > 0) else -ans

        