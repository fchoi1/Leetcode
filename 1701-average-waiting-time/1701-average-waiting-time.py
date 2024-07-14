class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        q = []
        N = len(customers)
        total = 0
        curr = 0
        for a,t in customers:
            if q:
                # while q[0][1] > a
                #     start,end = q.pop()
                #     total += (end - start)
                q.append((a, max(q[-1][1], a) + t))
            else:
                q.append((a, a+t))
        
        while q:
            start, end = q.pop()
            total += (end - start)
        # print("total", total)
        return total / N

        

        