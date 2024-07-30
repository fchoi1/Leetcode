class Solution:
    def minimumDeletions(self, s: str) -> int:
        start = 0
        

        def get_min(string):

            while start < len(s) - 1 and s[start] == 'a':
            start += 1
        end = len(s) - 1
        while end >= 0 and s[end] == 'b':
            end -= 1
            
            N = len(string) - 1

            start = 0 
            while start < len(string) - 1 and string[start] == 'b':
                start += 1
            end = N
            while end >= 0 and string[end] == 'a':
                end -= 1
            end_count = N - end - 1
            print(string, start, end, end_count)
            if start > end:
                return min(start, end_count) + get_min(string[start:end+1])

            return min(start, end_count)
        return get_min(s[start:end+1])