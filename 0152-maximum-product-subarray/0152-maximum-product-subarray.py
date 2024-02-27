class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        product = 1
        firstNeg = 1
        for n in nums:
            product *= n

            # If we hit a negative product that is not the first negative product, check
            if firstNeg < 0 and product < 0:
                maxP = max(maxP, product//firstNeg)

            # set first negative product we see
            if product < 0 and firstNeg > 0:
                firstNeg = product
            
            # check for max
            maxP = max(product, maxP)
            
            if n == 0:
                product = 1
                firstNeg = 1

        return maxP