class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # sort by total students and ratio
        # 
        h = []
        r = 0
        for p,t in classes:
            if p == t:
                r += 1
            else:
                heappush(h, (p/t-(p+1)/(t+1),t,p))

        i = 0
        while h and i < extraStudents:
            _, t, p = heappop(h)
            t += 1
            p += 1
            inc = p/t - (p+1)/(t+1)
            heappush(h, (inc, t,p))
            i += 1
        for _, t, p in h:
            r += p / t
        return r / len(classes)

        # 1/2
        # 2/3 

        # 2/4
        # 3/5 = 0.6