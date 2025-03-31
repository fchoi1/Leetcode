class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = sum(nums)
        n_set = Counter(nums)

        for outlier in nums:
            target = total - outlier
            
            if target % 2 == 1:
                continue
            if target // 2 in n_set:
                if outlier == target // 2 and n_set[target // 2] == 1:
                    continue
                return outlier

        return -1
        