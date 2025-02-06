class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        products = defaultdict(int)
        
        for i,a in enumerate(nums):
            for b in nums[i+1:]:
                products[a * b] += 1
        ans = 0
        for c in products.values():
            if c > 1:
                ans += c * (c - 1) // 2 * 8
        return ans