class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        H = len(mat)
        W = len(mat[0])


        prev = [0 for _ in range(W + 1)]
        prefixMat = [prev]
        for y in range(H):
            row = [0]
            curr = 0
            for x in range(W):
                curr = prev[x + 1] + mat[y][x]
                if x != 0:
                    curr += row[-1]
                    curr -= prev[x] 
                row.append(curr)
            prefixMat.append(row)
            prev = row
    

        def isValid(x,y,n):
            x += 1
            y += 1
            topLeft = prefixMat[y-1][x-1]
            topRight = prefixMat[y-1][x + n - 1]
            botLeft = prefixMat[y + n - 1][x - 1]
            botRight = prefixMat[y + n - 1][x + n - 1]

            # print(x,y,n)
            # print(topLeft, topRight, botLeft, botRight, "total", botRight + topLeft - topRight - botLeft )
            return botRight + topLeft -topRight - botLeft <= threshold

        for n in range(min(H,W), 0, -1):
            for y in range(H - n + 1):
                for x in range(W - n + 1):
                    if isValid(x,y,n):
                        return n
        return 0
