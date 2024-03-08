class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letters = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        path = ""
        for y, row in enumerate(board):
            for  x, val in enumerate(row):
                letters[val] = (x,y)
    
        start = letters['a']
        for char in target:
            x1,y1 = start
            x2,y2 = letters[char]

            xDiff = x2 - x1
            yDiff = y2 - y1
         
            if yDiff < 0:
                path += "U" * abs(yDiff)

            if xDiff < 0:
                path += "L" * abs(xDiff)

            if yDiff > 0:
                path += "D" * yDiff

            if xDiff > 0:
                path += "R" * xDiff

            path += "!"
            start = letters[char]
        return path
