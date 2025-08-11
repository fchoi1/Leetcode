class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        # prefix product

        p = []
        power = 1
        while n > 0:
            if n & 1:
                p.append(power)
            power *= 2
            n >>= 1
        product = [1]
        for val in p:
            product.append((val * product[-1]))
        
        arr = []
        for s,e in queries:
            arr.append((product[e + 1] // product[s])% mod)

        return arr 
        