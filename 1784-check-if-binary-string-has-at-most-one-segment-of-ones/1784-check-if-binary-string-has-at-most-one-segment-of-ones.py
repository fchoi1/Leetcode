class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        return len(s.replace('0',' ').strip().split(' ')) == 1