class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        letters = [0] * 26
        for char in s:
            letters[ord('z') - ord(char)] += 1

        fast = 0
        string = ''
        print(letters)
        for i in range(26):
            if letters[i] == 0:
                continue
            char = chr(ord("z") - i)
            print("char",char, i)
            

            while fast < len(letters) and  (fast <= i or letters[fast] == 0):
                fast += 1
            
            times, remain = divmod(letters[i], repeatLimit)
            if not remain:
                times -= 1

            for j in range(times):
                string += char * repeatLimit

                while fast < len(letters) and letters[fast] ==  0:
                    fast += 1
                    
                # No more replacement letters to add
                if fast >= len(letters):
                    return string
                
                string += chr(ord('z') - fast)
                letters[fast] -= 1

            string += char * remain

                
        return string

        # heap
