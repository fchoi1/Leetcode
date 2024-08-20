class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i = j = k = 0
        res = [1]
        while n > 1:
            val = min(2*res[i],3*res[j],5*res[k])
            if val == 2 * res[i]:
                i += 1
            if val == 3 * res[j]:
                j += 1
            if val == 5 * res[k]:
                k += 1
            res.append(val)
            n -= 1
        return res[-1]