class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        steps = i = 0

        while i < N:
            if i == N - 1:
                break
            currSteps = nums[i]
            if i + currSteps >= N - 1:
                return steps + 1
            print("at index", i, currSteps)

            furthest = currI = 0
            for j in range(currSteps):
                print("loop", j)
                if j + i + 1 >= N:
                    break
                if i + j + nums[j + i + 1] + 1 > furthest:
                    currI = j + 1
                    furthest = i + j + nums[j + i + 1] + 1 
                    print("found furthest", nums[j + i + 1], "currI",  currI )
            i += currI
            steps += 1
        return steps
