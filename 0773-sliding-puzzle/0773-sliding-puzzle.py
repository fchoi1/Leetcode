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
        

        q = [[*board[0], *board[1]]]
        seen = set()
        steps = 0
        while q:
            temp = []
            for position in q:
                if tuple(position) == solved:
                    return steps

                if tuple(position) in seen:
                    continue
                seen.add(tuple(position))

                pos = position.index(0) 
                for s in swaps[pos]:
                    new = position.copy()
                    new[pos], new[s] = new[s],new[pos]
                    temp.append(new)
            steps += 1
            q = temp
        return -1