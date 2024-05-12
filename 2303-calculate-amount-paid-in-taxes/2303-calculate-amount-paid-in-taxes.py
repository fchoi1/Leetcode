class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = prev = 0
        for i,(a,b) in enumerate(brackets):
            if income < a:
                tax += (income-prev) * b / 100
                return tax
            tax += (a-prev) * b / 100
            prev = a

        if income > prev:
            tax += (income-prev)*brackets[-1][1]
        return tax