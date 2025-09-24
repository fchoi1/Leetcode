def trunc_divmod(a, b):
    q = a // b    # truncate toward zero
    r = abs(a - b * q)
    return q, r

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = trunc_divmod(numerator, denominator)
        
        if b == 0:
            return str(a)

        sign = ''
        if a < 0:
            a = int(numerator/denominator)
            b = r = abs(numerator - denominator * a)
            sign = '-'

        # 333/4
        # 
        # 0.01

        # 400 - 333 = 67
        # 670 - 666 = 4
        # 40 -  =
        # 40
        # 

        # 2 / 1
        # 

        seen = {}
        repeat = ''
        divisor = abs(denominator) 
        dividend = abs(b * 10)
        remain = 0
        idx = 0
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
      
            q, remain = trunc_divmod(dividend, divisor)
            repeat += str(q)

            if remain == 0:
                return str(a) + '.' + repeat
            dividend = remain * 10
            idx += 1

        i = seen[dividend]

        return sign + str(a) + '.' + repeat[:i] + '(' + repeat[i:] + ')'
        