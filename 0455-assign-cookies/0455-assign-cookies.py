class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        count = child = cookie =  0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                count += 1
                cookie += 1
                child += 1
            else:
                while cookie < len(s) and s[cookie] < g[child]:
                    cookie += 1
        return count