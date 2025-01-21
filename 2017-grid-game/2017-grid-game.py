class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        top = []
        bot = []
        for a,b in zip(grid[0], grid[1][::-1]):
            if not top:
                top.append(a)
                bot.append(b)
            else:
                top.append(top[-1] + a)
                bot.append(bot[-1] + b)
        bot.reverse()
        
        top_total = top[-1]
        bot_total = bot[0]
        p2_min = inf

        for i, (a,b) in enumerate(zip(top,bot)):
            path_1 = top_total - a
            path_2 = bot_total - b
            p2_min = min(p2_min,max(path_1, path_2))
       
        return p2_min

