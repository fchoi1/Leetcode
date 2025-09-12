class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # partiion
        # backtrack

        N = len(s)

        # optimize?
        def isPali(string):
            return string[::-1] == string


        partitions = []
        def backtrack(index, parts):
            if index >= N:
                partitions.append(parts[::])
                return
            
            curr_str = ''
            for i in range(index,N):
                curr_str += s[i]
                if isPali(curr_str):
                    parts.append(curr_str)
                    backtrack(i + 1, parts)
                    parts.pop()

        backtrack(0, [])
        return partitions