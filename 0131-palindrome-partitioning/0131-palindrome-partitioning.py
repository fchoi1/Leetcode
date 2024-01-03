class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def checkPartitions(parts):
            parts = [0] + parts + [len(s)]
            arr = []
            for i in range(0, len(parts)-1):
                start = parts[i]
                end = parts[i+1]
                arr.append(s[start:end])
                if not isPali(s[start:end]):
                    return False, None
                prev = i
            return  True, arr
     

        def isPali(string):
            extra = (len(string) % 2 == 0) 
            return string[:len(string) // 2] == string[len(string):len(string) // 2-extra:-1]

        def backtrack(index,parts):
            isValid,arr = checkPartitions(parts)
            if isValid:
                res.append(arr)
                
            if index == len(s):
                return

            for i in range(index, len(s)):
                parts.append(i)
                backtrack(i+1, parts)
                parts.pop()
            pass
        backtrack(1,[])
        return res