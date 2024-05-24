class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        arr = []
        for i in range(0, half):
            arr.append(nums[i])
            arr.append(nums[i+half])
        return arr