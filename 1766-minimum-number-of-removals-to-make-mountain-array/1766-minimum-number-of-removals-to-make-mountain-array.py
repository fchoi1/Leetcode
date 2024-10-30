class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Combination of Longest Increasing Subsequence and Trapping Rain Water
        leftDP, rightDP = [1] * len(nums), [1] * len(nums)
        # Find LIS from left
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    leftDP[i] = max(leftDP[i], leftDP[j] + 1)
        # Find LIS from right
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    rightDP[i] = max(rightDP[i], rightDP[j] + 1)
        # Find largest mountain by finding largest sum
        ans = 0
        for i in range(len(nums)):
            # Make sure there is a left and right slope, or else it's not a mountain
            if (leftDP[i] != 1 and rightDP[i] != 1):
                ans = max(ans, leftDP[i] + rightDP[i])
        ''' Debugging purposes
        for i in leftDP:
            print(i)
        print("RIGHT")
        for j in rightDP:
            print(j)
        '''
        # Return the number of numbers to remove to form the mountain
        return len(nums) - ans + 1