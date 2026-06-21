class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = Counter(costs)
        ans = 0


        for c in range(1, max(counts) + 1):
            if coins < c:
                break

            bought = min(counts[c], coins // c)
            ans += bought
            coins -= c * bought

        return ans