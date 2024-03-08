class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letters = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        path = ""
        for y, row in enumerate(board):
            for  x, val in enumerate(row):
                letters[val] = (x,y)
        

        # left and down first
        # up and right 
        start = letters['a']
        for char in target:
            x1,y1 = start
            x2,y2 = letters[char]

            xDiff = x2 - x1
            yDiff = y2 - y1
         

            while yDiff < 0:
                yDiff += 1
                path += "U"

            while xDiff < 0:
                xDiff += 1
                path += "L"

            while yDiff > 0:
                yDiff -= 1
                path += "D"

            while xDiff > 0:
                xDiff -= 1
                path += "R"
            path += "!"
            start = letters[char]
        return path
