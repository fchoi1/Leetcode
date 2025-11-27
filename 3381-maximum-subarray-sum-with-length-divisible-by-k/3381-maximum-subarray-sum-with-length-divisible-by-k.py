class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # cycles

        # prefix sum

        # negatives

        # sliding window of length k

        # every k, do something take largest k 

        N = len(nums)
        curr = sum(nums[:k])
        k_arr = [curr]
        max_sum = curr
        for i in range(N - k):
            curr +=  -nums[i] + nums[i + k]
            max_sum = max(curr, max_sum)
            if i + 1 < k:
                k_arr.append(curr)
            else:
                idx = (i + 1) % k
                max_sum = max(max_sum,k_arr[idx], curr, curr + k_arr[idx])
                k_arr[idx] = max(curr, curr + k_arr[idx])

        print(k_arr)

        return max_sum