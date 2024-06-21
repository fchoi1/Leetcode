class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        total = sum(c if g == 0 else 0 for c,g in zip(customers, grumpy))
        maxCust = cust = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                cust += customers[i]
            
            if i >= minutes and grumpy[i-minutes] == 1:
                cust -= customers[i-minutes]
            maxCust = max(maxCust,cust)

        return total + maxCust