class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # get intersecting areas


        # 2 loops
        # check all intersecting areas?

        # bottom left, bottom right, top left, top right


        def isIntersection(sq1, sq2):
            bl_1, tr_1 = sq1
            bl_2, tr_2 = sq2
   

            return not (bl_1[0] > tr_2[0] or bl_2[0] > tr_1[0] or bl_1[1] > tr_2[1] or bl_2[1] > tr_1[1])


        def getIntersection(sq1, sq2):
            if not isIntersection(sq1, sq2):
                return 0

            bl_1, tr_1 = sq1
            bl_2, tr_2 = sq2
            x = min(tr_1[0], tr_2[0]) - max(bl_1[0], bl_2[0])
            y = min(tr_1[1], tr_2[1]) - max(bl_1[1], bl_2[1])
            return min(x,y) ** 2
            


        maxArea = 0
        N = len(bottomLeft)

        for i in range(N):
            bot1 = bottomLeft[i]
            top1 = topRight[i]

            for j in range(i + 1,N): 
                bot2 = bottomLeft[j]
                top2 = topRight[j]
                maxArea = max(maxArea, getIntersection((bot1, top1), (bot2, top2)))


        return maxArea