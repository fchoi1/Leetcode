class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        if len(nums) == 1:
            return nums
        gid = 0

        s = sorted(nums)
        currGroup = []
        pointer = []
        groups = []
        groupMap = {}

        for prev, curr in zip(s, s[1:]):
            groupMap[prev] = gid
            currGroup.append(prev)
            if curr - prev >limit:
                gid += 1
                groups.append(currGroup)
                currGroup = []
                pointer.append(0)

        currGroup.append(curr)
        groups.append(currGroup)
        pointer.append(0)
        groupMap[curr] = gid

        # print(groupMap)
        # print(pointer)
        # print(groups)

        ans = []
        for n in nums:
            gid = groupMap[n]
            index = pointer[gid]
            ans.append(groups[gid][index])

            pointer[gid] += 1
        
        return ans