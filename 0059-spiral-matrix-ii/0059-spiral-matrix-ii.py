class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        T = L = 0
        B = R = n -1
        c = 1
        while L <= R and T <= B:
            for i in range(L, R+1):
                grid[T][i] = c
                c += 1
            T += 1

            for i in range(T, B+1):
                grid[i][R] = c
                c += 1
            R -= 1

            for i in range(R, L-1, -1):
                grid[B][i] = c
                c += 1
            B -= 1

            for i in range(B, T-1, -1):
                grid[i][L] = c
                c += 1
            L+=1
        return grid
        