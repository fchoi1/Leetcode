from functools import reduce

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        for l, r, k, v in  queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % mod
                idx += k
        
        return reduce(lambda prev, curr: prev ^ curr, nums)
 