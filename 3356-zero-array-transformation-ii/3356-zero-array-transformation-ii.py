class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # update sum, intervals? how 
        # decrement the max amount

        # bin search len(nums) log len(queries)

        # keep max?

        # preprocess

        # sweep?
        currSum = 0
        pos = 0

        diff = [0 for _ in range(len(nums) + 1)]

        for i, n in enumerate(nums):

            # print("check", i, n, "currSum",currSum)

            while currSum < n:
                # print("update pos", pos, "currSum",currSum)
                if pos >= len(queries):
                    return -1

             
                l, r, dec = queries[pos]
                # if valid
                # print(l, r, i, "pos", pos)
                if l <= i <= r:
                    currSum += dec
                    # print("add sum", currSum)
                diff[l] += dec
                diff[r + 1] -= dec
                pos += 1
                # print("range", l, r, diff)
            else:
                currSum += diff[i + 1]
        return pos