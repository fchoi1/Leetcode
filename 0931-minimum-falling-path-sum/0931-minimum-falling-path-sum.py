class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp?
        # bottom up dp store the best per each row look below (x-1, x, x + 1) - borders


        # 2 1 3                                             -> (2 + 12) (1 + 12) (2 + 13) ->  14 13 15
        # 6 5 4 -> (6 + 7), (5 + 7),  (4 + 8) -> 13 12 12
        # 7 8 9 ->                            -> 7 8 9


        N = len(matrix)
        W = len(matrix[0])

        # start from bottom

        prev = [] # current row

        for i in range(N - 1, -1, -1):
            if i == N - 1:
                prev = matrix[i]
                continue
            curr = []
            for x in range(W):
                lowest = prev[x]

                if x - 1 >= 0:
                    lowest = min(lowest, prev[x-1])
                
                if x + 1 < W:
                    lowest = min(lowest, prev[x+1])

                curr.append(lowest + matrix[i][x])
            
            prev = curr
        
        return min(prev)
                


