class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        

        v_start = 0
        v_end = 0
        v_line = 0

        h_start = 0
        h_end = 0
        h_line = 0

        def check(dim):

            s_rect = sorted(rectangles, key=lambda x: x[dim])
            start = s_rect[0][0] if not dim else s_rect[0][1]
            end = s_rect[0][2] if not dim else s_rect[0][3]
            line = 0
            
            for x1,y1,x2,y2 in s_rect[1:]:
                if not dim:
                    s,e = x1, x2
                else:
                    s,e = y1, y2
                start = max(start, s)


                if end <= start:
                    line += 1
                    if line == 2:
                        return True

                end = max(end, e)
            return False

        return check(0) or check(1)

            
           