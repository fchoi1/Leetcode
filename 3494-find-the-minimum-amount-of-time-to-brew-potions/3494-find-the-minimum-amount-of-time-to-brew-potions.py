class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # when can the first wizard start,

        # determined but the longest wizard
        # find bottle neck for each cycle?

        # 5  30     40      60
        # +1 +5     +2      +4
        # 1   6      8      12
        # 6  11/31  39/41    45/61


        # 60 - 8  = 36
        # 61 - 12

        # 52  57   59     63


        # 2  12 16  24


        # for 1 potion
        prefix = []
        prev = []
        total = 0
        for s in skill:
            prefix.append(total)
            total += s
            prev.append(total * mana[0])
        prefix.append(total)
        print(prefix)
        print('start', prev)

        for m in mana[1:]:
            earliest = 0

            for time, p in zip(prefix, prev):
                earliest = max(earliest, p - time*m )

            prev = []
            for time in prefix[1:]:
                prev.append(time*m + earliest)


        return prev[-1]