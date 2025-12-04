class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        prev = None
        right = 0
        for d in directions:
            
            if d == 'L':
                if prev == 'L' or prev == None:
                    continue
                collisions += 1
                
                if prev == 'R':
                    collisions += right
     
                d = 'S'
                right = 0
            elif d == 'S' and prev == 'R':
                collisions += right
                right = 0
            elif d == 'R':
                right += 1
            
            prev = d
            

        return collisions