class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minPenalty = total = customers.count('Y')
        count = penalty = 0
        early = 0
        for i,c in enumerate(customers):
            if c == 'Y':
                count += 1
            if c == 'N':
                penalty += 1
            if penalty + total - count < minPenalty:
                minPenalty = penalty + total - count
                early = i + 1
 

        return early