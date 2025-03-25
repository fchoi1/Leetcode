class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        rectangles.sort()

        v_start = 0
        v_end = 0
        v_line = 0

        h_start = 0
        h_end = 0
        h_line = 0

        for x1,y1,x2,y2 in rectangles[1:]:

            # check at each start
            v_start = max(v_start, x1)

            if v_end <= v_start:
                lines += 1
                if line == 2:
                    return True

            v_end = max(v_end, x2)

            v_start = max(v_start, x1)

            if v_end <= v_start:
                lines += 1
                if line == 2:
                    return True

            v_end = max(v_end, x2)
        return False

            
           