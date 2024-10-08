class Solution:
    def minSwaps(self, s: str) -> int:
        # count open brackets not closed?
        opened = 0
        swap = 0
        for b in s:
            # print(opened)
            if opened < 0:
                swap += 1
                opened = 0
            opened += 1 if b == "[" else -1
        return math.ceil(swap / 2)

