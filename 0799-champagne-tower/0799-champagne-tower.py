class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # we need to know after each row how much over spills
        # subract 1  if over then we append it, else none, also this is symetric, calc half?

        if query_row == 0:
            return min(1, poured)
            
        remain = [max(0, poured - 1) / 2] # cup pouring to next level
        for row in range(query_row):
            new = []

            for i,r in enumerate(remain):
                if i == 0:
                    total = r
                else:
                    total = remain[i - 1] + r
                                
                if row + 1 == query_row and i == query_glass:
                    return min(1, total)
                
                if total > 1:
                    new.append((total - 1) / 2)
                else:
                    new.append(0)

            if row + 1 == query_row and len(remain) == query_glass:
                return min(1, remain[-1])
            new.append((remain[-1] - 1) / 2 if remain[-1] > 1 else 0)
            remain = new
            row += 1

        return 0