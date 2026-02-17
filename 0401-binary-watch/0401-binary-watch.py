class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # go through 0 - 11
        # go throught minues

        ans = []
        for hour in range(12):
            for minute in range(60):
                bit = hour.bit_count() + minute.bit_count()

                if bit == turnedOn:
                    ans.append(f"{str(hour)}:{str(minute).zfill(2)}")
        return ans