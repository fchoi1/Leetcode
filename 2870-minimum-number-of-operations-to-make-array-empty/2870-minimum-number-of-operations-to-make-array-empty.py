class Solution:
    def minOperations(self, nums):
        n = len(nums)
        cnt = 0
        freq = Counter(nums)

        # Iterate through the frequencies and calculate operations
        for val in freq.values():
            # If the frequency is 1, it's not possible
            if val == 1:
                return -1

            # Calculate operations based on the frequency
            if val % 3 == 0:
                cnt += val // 3
            else:
                # If the remainder is 1 or 2 after dividing by 3
                cnt += val // 3 + 1

        return cnt