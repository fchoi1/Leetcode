class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        d_sum = []

        for n in nums:
            d_sum.append((sum(int(digit) for digit in str(n)),n))


        sorted_dict = {k[1]:i for i,k in enumerate(sorted(d_sum))}
    

        seen = set()
        swaps = 0
        for i,n in enumerate(nums):
            if sorted_dict[n] == i:
                continue

            curr = n
            loop = 0
            # print('start', curr)
            while curr not in seen:
                seen.add(curr)
                index = sorted_dict[curr]
                curr = nums[index]
                loop += 1
            #     print("curr", curr)
            # print("done", loop)
            swaps += max(0, loop - 1)
        return swaps