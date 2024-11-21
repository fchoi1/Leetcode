class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 4 passes
        # row
        wallSet = set()
        guardSet = set()

        for x,y in walls:
            wallSet.add((y,x))
        for x,y in guards:
            guardSet.add((y,x))

        forward = set()
        backward = set()
        top = set()
        bottom = set()
        for y in range(m):
            seen = set()
            for x in range(n):
                if (x,y) in wallSet:
                    forward.update(seen)
                    seen = set()
                elif (x,y) in guardSet:
                    seen = set()
                else:
                    seen.add((x,y))
            forward.update(seen)

            seen = set()
            for x in range(n-1,-1,-1):
                if (x,y) in wallSet:
                    backward.update(seen)
                    seen = set()
                elif (x,y) in guardSet:
                    seen = set()
                else:
                    seen.add((x,y))
            backward.update(seen)

        for x in range(n):
            seen = set()
            for y in range(m):
                if (x,y) in wallSet:
                    top.update(seen)
                    seen = set()
                elif (x,y) in guardSet:
                    seen = set()
                else:
                    seen.add((x,y))
            top.update(seen)
                    
            seen = set()
            for y in range(m-1,-1,-1):
                if (x,y) in wallSet:
                    bottom.update(seen)
                    seen = set()
                elif (x,y) in guardSet:
                    seen = set()
                else:
                    seen.add((x,y))
            bottom.update(seen)

        valid = set.intersection(top, bottom, forward, backward)
        return len(valid) 

                
        # forwards
        # backwards

        # col
        