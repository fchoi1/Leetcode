class Solution:
    def sumZero(self, n: int) -> List[int]:
        even = n % 2 == 0
        pos = list(range(1,n//2+1))
        neg = list(range(-1, -n//2-int(even), -1))
        return pos + neg if even else pos + neg + [0]

        