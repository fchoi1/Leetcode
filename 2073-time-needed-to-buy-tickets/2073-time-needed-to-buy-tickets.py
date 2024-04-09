class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # for vals < tickets[k] = time lese

        time = 0
        val = tickets[k]
        for i, t in enumerate(tickets):
            if i > k:
                time += min(val-1, t)
            else:
                time += min(val, t)
        # 24 24 5 24 24 24 24  8 
        return time