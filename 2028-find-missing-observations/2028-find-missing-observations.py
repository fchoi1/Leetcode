class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        missing = total * mean - sum(rolls)

        times = missing / n
        if times < 1 or times > 6:
            return []
        times = int(times)
        diff = missing - times * n

        ans = [times] * n

        print(times, missing, n, diff)
        if diff > 0:
            for i in range(n):
                if diff == 0:
                    return ans
                
                add = 6 - ans[i]
                ans[i] += min(add,diff)
                diff -= min(add,diff)


        return ans

        
