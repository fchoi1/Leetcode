class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        N = len(nums)
        slow = c = 0 
        total = N * (N + 1) // 2
        
        for i, n in enumerate(nums):
            print(i, c)
            count[n] += 1
            while len(count) > k:
                count[nums[slow]] -= 1
                if count[nums[slow]] == 0:
                    del count[nums[slow]]
                slow += 1
            if len(count) == k:
                s = set()
                for l in range(i,slow-1, -1):
                    s.add(nums[l])
                    if len(s) == k:
                        c += l - slow + 1
                        break
        print(total, c)
        return c

        # 1 1 2 2 3
        # 0 0 2 2 2
        #       4 6

        # 1 2 1 2 3
        # 0 1 2 3 1
        