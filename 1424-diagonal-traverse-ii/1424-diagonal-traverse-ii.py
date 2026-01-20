class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # down left 
        # botto row

        values = defaultdict(list)

        H = len(nums)
        for y in range(H):
            W = len(nums[y])

            for x in range(W):
                val = x + y

                values[val].append((x, y, nums[y][x]))

        
        sortedVals = sorted(values.items())

        ans = []
        for _, vals in sortedVals:
            ans.extend([row[2] for row in sorted(vals)])
        
        return ans