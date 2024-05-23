class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        def checkSubset(index, arr):
            nonlocal res
            if arr:
                res += 1
            
            for i in range(index, len(nums)):
                if nums[i] + k in arr or nums[i] - k in arr:
                    continue
                arr.append(nums[i])
                checkSubset(i + 1, arr)
                arr.pop()

        checkSubset(0,[])
        print(res)
        return res
        