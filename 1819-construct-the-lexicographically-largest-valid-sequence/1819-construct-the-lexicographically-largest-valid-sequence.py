class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        self.ans = None

        def backtrack(index, arr, avail):

            if len(avail) == 0:
                self.ans = arr[::]
                return True

            while index < len(arr) and arr[index] != 0:
                index += 1

            if index >= len(arr):
                return False

            # start from highest
            for curr in range(max(avail),0,-1):
                if curr not in avail:
                    continue
                if (index + curr < len(arr) and arr[index + curr] == 0) or curr == 1:
                    avail.remove(curr)
                    arr[index] = curr
                    if curr != 1:
                        arr[index + curr] = curr

                    if backtrack(index + 1, arr, avail):
                        return True
                    if curr != 1:
                        arr[index + curr] = 0
                    arr[index] = 0
                    avail.add(curr)
            return False

        arr = [0] * (n * 2 - 1)
        backtrack(0, arr, set(range(1, n + 1)))

        return self.ans