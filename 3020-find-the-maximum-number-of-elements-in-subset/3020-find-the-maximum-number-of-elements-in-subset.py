from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0

        # Handle 1 separately
        if 1 in counts:
            ans = max(ans, counts[1] if counts[1] % 2 == 1 else counts[1] - 1)

        for n in counts:
            if n == 1:
                continue

            curr = 0
            x = n

            while True:
                if counts[x] >= 2:
                    curr += 2
                    x = x * x
                elif counts[x] == 1:
                    curr += 1
                    break
                else:
                    # We ended after taking a pair, so one of that pair
                    # must become the center (remove one element).
                    if curr > 0:
                        curr -= 1
                    break

            ans = max(ans, curr)

        return ans