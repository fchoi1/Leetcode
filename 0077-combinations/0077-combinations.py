class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def getCombo(arr, i):
            if len(arr) == k:
                res.append(arr.copy())
                return
            for num in range(i + 1, n + 1):
                arr.append(num)
                getCombo(arr, num)
                arr.pop()

        getCombo([], 0)
        return res
