class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = []
        count = 0
        for i, val1 in enumerate(arr[:-2]):
            for j, val2 in enumerate(arr[i+1:-1]):
                for val3 in arr[i+j+2:]:
                    if abs(val1 - val2) <= a and abs(val2 - val3) <= b and abs(val1 - val3) <= c:
                        count += 1
        return count
        