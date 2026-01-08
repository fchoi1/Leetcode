class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        target = [0] + target
        for prev,curr in zip(target, target[1:]):
            diff = curr - prev - 1
            for _ in range(diff):
                ans.extend(["Push", "Pop"])
            ans.append("Push")

        return ans