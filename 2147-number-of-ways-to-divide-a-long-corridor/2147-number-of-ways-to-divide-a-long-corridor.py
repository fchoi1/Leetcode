class Solution:
    def numberOfWays(self, corridor: str) -> int:
        c = corridor.count('S')
        if c % 2 == 1 or c == 0:
            return 0

        firstSeat = False
        first = last = -1
        ans = 1
        mod = 10 ** 9 + 7
        for i, val in enumerate(corridor):
            if val == 'P':
                continue

            if not firstSeat:
                first = i
                # check combos
                if last != -1:
                    # print("first, last", first, last, firstSeat)
                    combo =  first - last
                    ans *= combo
                    ans %= mod
            else:
                last = i
            
            firstSeat = not firstSeat

            # dist between last and first
        

        return ans % mod
        