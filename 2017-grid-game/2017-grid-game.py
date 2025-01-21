class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # 2 bfs
        # first optimal, highest cost
        # second optimal, highest cost

        # 2x2

        # 1 1 1 2 1
        # 1 2 1 1 1 

        # prefix

        N =  len(grid[0])
        def getPrefix(arr):
            pre_1 = []
            pre_2 = []
            for a,b in zip(arr[0], arr[1][::-1]):
                if not pre_1:
                    pre_1.append(a)
                    pre_2.append(b)
                else:
                    pre_1.append(pre_1[-1] + a)
                    pre_2.append(pre_2[-1] + b)
            pre_2.reverse()
            return pre_1, pre_2

        # get switch index
        player1_1, player1_2 = getPrefix(grid)
        switch = 0
        curr = player1_1[0] + player1_2[0]
        for i, (a,b) in enumerate(zip(player1_1,player1_2)):
            if a + b > curr:
                curr = a + b
                switch = i

        # update grid
        for i in range(N):
            if i <= switch:
                grid[0][i] = 0
            
            if i >= switch:
                grid[1][i] = 0

        player2_1, player2_2 = getPrefix(grid)


        return max(a + b for a,b in zip(player2_1, player2_2))
