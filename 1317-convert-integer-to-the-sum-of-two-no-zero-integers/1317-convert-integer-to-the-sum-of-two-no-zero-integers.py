class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if str(i).count('0') == 0 and str(n-i).count('0') == 0:
                return [i,n-i]