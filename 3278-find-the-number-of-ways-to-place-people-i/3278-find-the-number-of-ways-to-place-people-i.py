class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # negative slope? and no points inside?
        #  when is ?

        #  x1 > x2, and y1 < y2
        #  x1 < x2 and y1 > y2

        points.sort(key=lambda x: (x[0], -x[1]))  # x, y
        # for each point:
            # loop once to check if less
            # also check if in rect? 50
            # check seen points

        N = len(points)
        count = 0
        for i in range(N):
            x1, y1 = points[i]
            seen = set()
            for j in range(i + 1, N):
                x2, y2 = points[j]

                if y1 >= y2:
                    for seenX, seenY in seen:
                        if x1 <= seenX <= x2 and y2 <= seenY <= y1:
                            break
                    else:
                        count += 1
                
                seen.add((x2,y2))
        return count
            


        