class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:


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
            return pre_1, pre_2, pre_1[-1], pre_2[0]

        # get switch index
        top, bot, top_total, bot_total = getPrefix(grid)
        switch = 0
        curr = top[0] + bot[0]
        p2_curr = 0
        p2_min = inf
        for i, (a,b) in enumerate(zip(top,bot)):


            t = top_total - a
            b = bot_total - b

            p2_min = min(p2_min,max(t,b))
            # bot
            if a + b > curr:
                curr = a + b
                switch = i
        return p2_min

