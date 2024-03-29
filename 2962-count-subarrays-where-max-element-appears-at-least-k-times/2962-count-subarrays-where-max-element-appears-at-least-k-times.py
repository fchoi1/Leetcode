class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # heap 
        # hash

        # once we find an array that satisfies it, the rest do as well and all previous ones too
        # might well count the subarrays that dont have k
        #

        # total subarrays len(n)
        n = len(nums)
        maxEl = max(nums)
        print("len", n)
        total = n * (n+1) // 2
        
        counts = 0
        slow = 0
        neg = 0
        for i, n in enumerate(nums):
            if n == maxEl:
                counts += 1
            while counts >= k:
                if nums[slow] == maxEl:
                    counts -= 1
                slow += 1
            neg += i - slow + 1
        return total - neg


        # 1 3 1 2
        # 
            




 