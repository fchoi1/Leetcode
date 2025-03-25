class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # check horizontal
        
        # check vertical

        # O(N)

        vert = [[0,0] for _ in range(n + 1)]
        hori = [[0,0] for _ in range(n + 1)]

        for a,b,x,y in rectangles:
            vert[a][0] += 1
            vert[x][1] += 1
            hori[b][0] += 1
            hori[y][1] += 1

        curr = prev = 0
        lines = 0

        for start, end in vert:

            curr -= end
            if curr == 0 and prev != 0:
                lines += 1
                if lines == 3:
                    return True
            curr += start
            prev = curr

        
        curr = prev = 0
        lines = 0

        for start, end in hori:
            curr -= end
            if curr == 0 and prev != 0:

                lines += 1
                if lines == 3:
                    return True
            curr += start
            prev = curr
        return False
