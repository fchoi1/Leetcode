class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [(p, h, d,i) for i,(p,h,d)in enumerate(zip(positions, healths, directions))]

        robots.sort()

        # optimization remove robots on the left and right
        # going from left to right
        # store left robots in dict
        # counter to store health?
        # q
        print(robots)
        left = []
        remain = []
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
                remain.append([h,i])
                
            if d == 'R':
                left.append([h,i])
            # print(left, remain)

            

        for h,i in left:
            remain.append([h,i])

        remain.sort(key=lambda x:x[1])
        return [h for h,i in remain]
        