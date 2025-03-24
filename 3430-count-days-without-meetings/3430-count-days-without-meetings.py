class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        total = prevEnd = 0

        for start,end in meetings:
            if start > prevEnd:
                total += start - prevEnd - 1
            prevEnd = max(end,prevEnd)
        
        total += days - prevEnd 
        return total
        