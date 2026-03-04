class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                if val:
        
                    if x in rows or y in cols:
                        rows[x] = -1
                        cols[y] = -1

                    if rows[x] == -1 or cols[y] == -1:
                        continue

                    rows[x] = 1
                    cols[y] = 1
        print(rows, cols)
        return sum(c == 1 for c in rows.values())

        