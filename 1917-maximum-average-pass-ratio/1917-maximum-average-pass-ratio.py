class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratios = []
        perfect = 0
        for p,c in classes:
            if c == p:
                perfect += 1
                continue
            inc = (p+1)/(c+1) - p/c
            heappush(ratios, (-inc, c, p))

        if len(ratios) == 0:
            return 1

        for i in range(extraStudents):
            _, c, p = heappop(ratios)
            p +=1
            c += 1
            inc = (p+1)/(c+1) - p/c
            heappush(ratios, (-inc,c,p))

        return (sum(p/c for _,c,p in ratios) + perfect) / len(classes)

        
        