class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtrack / dfs

        self.solutions = []
    
        def placeQueen(row, col, taken):
            for i in range(n):
                taken.add((row,i))
                taken.add((i,col))
                if row + i < n and col + i < n:
                    taken.add((row + i, col + i))
                    
                if row - i >= 0 and col - i >= 0:
                    taken.add((row - i, col - i))

                if row + i < n and col - i >= 0:
                    taken.add((row + i, col - i))

                if row - i >= 0 and col + i < n:
                    taken.add((row - i, col + i))
            return taken

        def getTaken(queens):
            taken = set()
            for x,y in queens:
                taken = placeQueen(x,y,taken)
            return taken

        def buildSolution(positions):
            ans = []
            for i in range(n):
                row = ''
                for j in range(n):
                    if positions[i] == (i,j):
                        row += 'Q'
                    else:
                        row += '.'
                ans.append(row)
            return ans
        
        def backtrack(queens, positions):
            if queens >= n:
                self.solutions.append(buildSolution(positions))
                return
            
            taken = getTaken(positions)

            # start at ith row
            for i in range(n):
                if (queens,i) not in taken:
                    positions.append((queens,i))
                    backtrack(queens + 1, positions)
                    positions.pop()



        board = [[0 for _ in range(n)] for _ in range(n)]
        # 0 - free
        # 1 - queen
        # 2 - not free
        backtrack(0,[])
        ans = []
        


        return self.solutions