class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        p_y = defaultdict(int)
        p_y_sum = defaultdict(int)

        mod = 10 ** 9 + 7

        for x,y in points:
            if p_y[y] > 0:
                p_y_sum[y] += p_y[y]
            p_y[y] += 1

        ans = curr = 0
        for count in p_y_sum.values():
            ans = (ans + curr * count) % mod
            curr += count

        
        return ans