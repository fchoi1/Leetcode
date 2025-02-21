class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        steps = i = 0

        while i < N - 1:
            currSteps = nums[i]
            furthest = currI = 0
            if i + currSteps >= N - 1:
                return steps + 1

            for j in range(i + 1, min(i + currSteps + 1, N)):
                if j + nums[j] > furthest:
                    currI = j 
                    furthest = j + nums[j] 

            i = currI
            steps += 1

        return steps
