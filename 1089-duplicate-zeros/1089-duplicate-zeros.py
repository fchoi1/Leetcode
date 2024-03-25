class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        i = zeros = 0
        q = deque([])
        while i < len(arr):
            q.append(arr[i])

            if zeros > 0:
                arr[i] = 0
                zeros -= 1
            else:
                if q[0] == 0:
                    zeros += 1
                arr[i] = q.popleft()
            i += 1
