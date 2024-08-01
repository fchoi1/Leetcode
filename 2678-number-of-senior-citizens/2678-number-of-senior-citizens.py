class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old = 0
        for d in details:
            if int(d[-4:-2]) > 60:
                old += 1
        return old
        