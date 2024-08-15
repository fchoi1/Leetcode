class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for bill in bills:
            diff = bill - 5
            change[bill] += 1
            if diff == 0:
                continue
            elif diff == 5 and change[5] > 0:
                change[5] -= 1
            elif diff == 15 and change[10] > 0 and change[5] > 0:
                change[5] -= 1
                change[10] -= 1
            elif diff == 15 and change[5] > 2:
                change[5] -= 3
            else:
                return False

        return True

