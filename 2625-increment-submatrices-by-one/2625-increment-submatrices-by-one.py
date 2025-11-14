class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        mat = [[0 for _ in range(n)] for _ in range(n)]

        for y1, x1, y2, x2 in queries:
            for y in range(y1, y2 + 1):
                mat[y][x1] += 1
                if x2 + 1 < n:
                    mat[y][x2 + 1] -= 1
    
        ans = []
        for y in range(n):
            curr = 0
            row = []
            for x in range(n):
                curr += mat[y][x]
                row.append(curr)
            ans.append(row)

        return ans


