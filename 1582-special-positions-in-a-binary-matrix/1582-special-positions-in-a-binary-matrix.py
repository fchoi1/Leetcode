class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        points = set()

        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                if val:
                    rows[x] += 1
                    cols[y] += 1
                    points.add((x,y))

        return sum(rows[x] == 1 and cols[y] == 1 for x,y in points)
        

        