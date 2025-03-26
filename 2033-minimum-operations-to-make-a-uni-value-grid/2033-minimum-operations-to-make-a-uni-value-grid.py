class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # divisble?
        # multiple 
        # get avg?
        
        def getPrefix(arr):
            prefix = [0]
            prev = base = arr[0]
            
            for i, n in enumerate(arr):
                if (n - base) % x != 0:
                    return None
                remain = abs(n - prev) // x
                prev = n
                prefix.append(prefix[-1] + remain * i)
            return prefix

        flat = [item for row in grid for item in row]

        if len(flat) == 1:
            return 0
        flat.sort()

        left = getPrefix(flat)
        if not left:
            return -1
        right = getPrefix(flat[::-1])

        
        # median
        even = (len(left) - 1) % 2 == 0
        mid = len(left) // 2
        l = mid
        r = mid + 1 if even else mid

        
        return left[l] + right[r]