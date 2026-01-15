class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        N = len(nums)
        closest = sum(nums[:3])

        for i in range(N):
            n1 = nums[i]

            l = i + 1
            r = N - 1

            
            while l < r:
                curr = nums[l] + nums[r] + n1

                diff = abs(target - closest)
                currDiff = abs(target - curr)

                if currDiff == 0:
                    return target

                if currDiff < diff:
                    closest = curr

                if curr > target:
                    r -= 1
                else:
                    l += 1
             


                
                


        return closest