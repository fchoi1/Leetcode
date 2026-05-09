from collections import defaultdict, deque

class Solution:
    def build_spf(self, n):
        spf = list(range(n + 1))
        spf[1] = 1

        for i in range(2, int(n ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        return spf

    def is_prime(self, x, spf):
        return x > 1 and spf[x] == x

    def get_factors(self, x, spf):
        res = set()
        while x > 1:
            res.add(spf[x])
            x //= spf[x]
        return res

    def minJumps(self, nums):
        n = len(nums)
        spf = self.build_spf(max(nums))

        # prime â indices where nums[j] % prime == 0
        prime_map = defaultdict(list)

        for i, val in enumerate(nums):
            for p in self.get_factors(val, spf):
                prime_map[p].append(i)

        visited = [False] * n
        q = deque([(0, 0)])
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # adjacent moves
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))

            # teleport ONLY if nums[i] is prime
            val = nums[i]
            if self.is_prime(val, spf) and val not in used_prime:
                used_prime.add(val)

                for ni in prime_map[val]:
                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, steps + 1))

                prime_map[val] = []

        return -1