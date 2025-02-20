class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        maxN = 2 ** N 

        curr = set()
        for n in nums:
            curr.add(int(n,2))

        for i in range(maxN):
            if i not in curr:
                return bin(i)[2:].zfill(N)

        return "error"