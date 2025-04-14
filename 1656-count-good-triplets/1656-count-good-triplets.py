class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        good = 0
        for i in range(N):
            for j in range(i + 1, N):
                if abs(arr[j] - arr[i]) > a:
                    continue
                for k in range(j + 1, N):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        good += 1
        return good 
        