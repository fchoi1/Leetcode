
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = divmod(numerator, denominator)
        
        if b == 0:
            return str(a)

        # Edge case negative
        sign = ''
        if a < 0:
            a = int(numerator/denominator)
            b = abs(numerator - denominator * a)
            sign = '-'


        seen = {}
        repeat = ''
        divisor = abs(denominator) 
        dividend = abs(b * 10)
        remain = idx = 0

        while dividend not in seen:
            seen[dividend] = idx
            count = 0
            while dividend < divisor:
                repeat += '0'
                dividend *= 10
                if dividend in seen:
                    i = seen[dividend]
                    return str(a) + '.' + repeat[:i] + '(' + repeat[i:] + ')'
                idx += 1
                seen[dividend] = idx
      
            q, remain = divmod(dividend, divisor)
            repeat += str(q)

            if remain == 0:
                return str(a) + '.' + repeat
            dividend = remain * 10
            idx += 1

        i = seen[dividend]

        return sign + str(a) + '.' + repeat[:i] + '(' + repeat[i:] + ')'
        