class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        product = 1
        firstNeg = 1
        for n in nums:
            product *= n
            if firstNeg < 0 and product < 0:
                maxP = max(maxP, product//firstNeg)
            if product < 0 and firstNeg > 0:
                firstNeg = product
            maxP = max(product, n, maxP)
            
            if n == 0:
                product = 1
                firstNeg = 1

        return maxP