class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # divisble?
        # multiple 
        # get avg?
        
        # no need for prefix
        def getHalf(arr, isLeft=True):
            curr = 0
            prev = base = arr[0]
            odd = len(arr) % 2 == 1
            mid = len(arr) // 2 + 1 if isLeft or odd else len(arr) // 2

            for i, n in enumerate(arr[:mid]):
                if (n - base) % x != 0:
                    return -1
                remain = abs(n - prev) // x
                prev = n
                curr += remain * i
            return curr

        flat = [item for row in grid for item in row]

        if len(flat) == 1:
            return 0

        flat.sort()

        left = getHalf(flat)
        right = getHalf(flat[::-1], False)

        if left == -1 or right == -1:
            return -1
            
        return left + right