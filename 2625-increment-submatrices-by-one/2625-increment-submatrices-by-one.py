class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # store this data?
        # return matrix


        # track each of the four corners
        # +1 for left bottom and left top
        # -1 for right bottom and right top
        queries.sort()
        
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for y1, x1, y2, x2 in queries:
            for y in range(y1, y2 + 1):
                mat[y][x1] += 1
                if x2 + 1 < n:
                    mat[y][x2 + 1] -= 1
    
        ans = [[0 for _ in range(n)] for _ in range(n)]
        for y in range(n):
            curr = 0
            for x in range(n):
                curr += mat[y][x]
                ans[y][x] = curr

    
        return ans


