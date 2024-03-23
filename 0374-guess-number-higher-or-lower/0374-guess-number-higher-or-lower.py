# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        mid = (l + r) // 2
        g = guess(mid)
        while g != 0:
            print(g, l, r)
            if g == -1:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r)//2
            g = guess(mid)
        return mid
        