class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        # get each diag, sort and replace?
        N = len(grid)
        def getDiag(start, reverse):
            x,y = start
            arr = []
            while x < N and y < N:
                arr.append(grid[y][x])

                x += 1
                y += 1


            return sorted(arr,reverse=reverse)

        
        def replaceDiag(start, arr):
            x,y = start
            i = 0
            while x < N and y < N:
                grid[y][x] = arr[i]
                x += 1
                y += 1
                i += 1

        
        for i in range(N):
            decrease = (0, i)
            increase = (i + 1, 0)
            arr_d = getDiag(decrease, True)
            arr_i = getDiag(increase, False)

            replaceDiag(decrease, arr_d)
            replaceDiag(increase, arr_i)
        
        return grid