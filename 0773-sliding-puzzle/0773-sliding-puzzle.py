class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        # brute force cache

        seen = {}

        solved = (1,2,3,4,5,0)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        self.ans = inf

        swaps = [(1,3), (0,2,4), (1,5), (0,4), (1,3,5), (2,4)]

        def dfs(position, steps):
            if tuple(position) == solved:
                self.ans = min(self.ans, steps)
                return 

            if tuple(position) in seen and steps > seen[tuple(position)]:
                return 
            seen[tuple(position)] = steps

            pos = position.index(0) 
            for s in swaps[pos]:
                new = position.copy()
                new[pos], new[s] = new[s],new[pos]
                dfs(new, steps + 1)
        
        dfs([*board[0], *board[1]], 0)
            
        return self.ans if self.ans != inf else -1