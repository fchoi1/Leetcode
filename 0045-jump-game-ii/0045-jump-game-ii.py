class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        steps = i = 0

        while i < N - 1:
            currSteps = nums[i]
            furthest = currI = 0

            if i + currSteps >= N - 1:
                return steps + 1

            for j in range(currSteps):
                if j + i + 1 >= N:
                    break

                if i + j + nums[j + i + 1] + 1 > furthest:
                    currI = j + 1
                    furthest = i + j + nums[j + i + 1] + 1 

            i += currI
            steps += 1

        return steps
