class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # radius
        ans = []
        for x,y,r in queries:
            c = sum(math.sqrt(abs(x2-x) ** 2 + abs(y2-y) ** 2)<= r for x2, y2 in points)
            # for x2,y2 in points:
            #     r_check = math.sqrt(abs(x2-x) ** 2 + abs(y2-y) ** 2)
            ans.append(c)
        return ans

        