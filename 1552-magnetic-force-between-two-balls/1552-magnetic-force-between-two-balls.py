class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # ,ax
        # 
        position.sort()
        r = position[-1]
        l =  1
        print(l, r)
        while l < r:
            mid = (l + r) // 2
            prev = position[0]
            count = 1
            for p in position:
                if p - prev >= mid:
                    count += 1
                    prev = p
            # print("count", count)
            if count < m:
                r = mid 
            else:
                l = mid + 1
            # print(l, r, mid)
        print(l, r)
        return l - 1