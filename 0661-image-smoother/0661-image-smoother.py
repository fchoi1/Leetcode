class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        w = len(img[0])
        h = len(img)
        def getAvg(x,y):
            c = total = 0
            for j in [y-1, y, y+1]:
                for i in [x-1, x, x+1]:
                    if 0 <= i < w and 0 <= j < h:
                        c += 1
                        total += img[j][i]
            return total // c
        new =  []
        for y in range(h):
            row = []
            for x in range(w):
                row.append(getAvg(x,y))
            new.append(row)
        return new

        