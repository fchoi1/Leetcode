class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = Counter(costs)

        s_c = sorted(counts.items())

        ans = 0
        curr = coins
        for c, q in s_c:
            if curr < c:
                break

            bought = min(q, curr // c)
            ans += bought
            curr -= c * bought

        return ans