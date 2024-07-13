class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([(p, h, d,i) for i,(p,h,d)in enumerate(zip(positions, healths, directions))])

        left = []
        remain = [0] * len(positions)
        for p,h,d,i in robots:
            if left and d == 'L':
                while left and h > left[-1][0]:
                    left.pop()
                    h -= 1
                
                if left and h == left[-1][0]:
                    h = 0
                    left.pop()
                elif left:
                    h = 0
                    left[-1][0] -= 1
            
            if not left and d == 'L' and h > 0:
                remain[i] = h
                
            if d == 'R':
                left.append([h,i])

        for h,i in left:
            remain[i] = h

        return  filter(lambda h: h > 0, remain)
        