class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        q = []
        N = len(customers)
        total = 0
        curr = end = 0
        for a,t in customers:
            end = max(end + t, a + t)
            # if q:
            #     while q and a >= q[0][1]:
            #         start, end = q.pop()
            total += (end - a)
            # q.append((a, end+t))
            print(q)
      
        return total / N

        

        