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
        flat.sort()

        left = getPrefix(flat)
        if not left:
            return -1
        right = getPrefix(flat[::-1])


        l = 1
        r = len(right) - 1
        ops = inf
        while l < len(left):
            ops = min(ops, left[l] + right[r])
            r -= 1
            l += 1

        
        
        print(left)
        print(right)

    
        return ops