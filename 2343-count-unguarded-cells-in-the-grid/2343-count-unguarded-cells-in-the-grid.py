class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = set()
        w_set = set()
        
        for x,y in walls:
            guarded.add((x,y))
            w_set.add((x,y))

        for x,y in guards:
            guarded.add((x,y))
            w_set.add((x,y))

        for x, y in guards:
            for dx,dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                i = 1
                while True:
                    nx, ny = dx * i + x, dy * i + y

                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in w_set:
                        guarded.add((nx,ny))
                    else:
                        break
                    i += 1

        return m * n - len(guarded)
        