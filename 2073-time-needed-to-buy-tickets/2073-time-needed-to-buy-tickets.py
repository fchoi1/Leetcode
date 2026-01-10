class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]

        time = 0
        for i,t in enumerate(tickets):
            time += min(t, target) if i <= k else min(t, target-1)
            
        return time