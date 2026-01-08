class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        N = len(nums) // 2
        ans = []
        for x,y in zip(nums[:N], nums[N:]):
            ans.extend([x,y])
        return ans