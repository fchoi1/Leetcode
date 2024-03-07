class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        letters = [0] * 26

        # bucket sort
        for char in s:
            letters[ord("z")-ord(char)] += 1

        # replacement pointer 
        fast = 0
        string = ""
        for i in range(26):
            if letters[i] == 0:
                continue
            char = chr(ord("z") - i)

            # Update replacement pointer to a different non-empty character than current         
            while fast < len(letters) and (fast == i or letters[fast] == 0):
                fast += 1
            
            # get cycles and remainder
            subtract, remain = divmod(letters[i], repeatLimit)
            
            for i in range(subtract):
                string += char * repeatLimit

                # edge case when remainder is zero, no need to add replacement pointer
                if i == subtract - 1 and remain == 0:
                    break

                # Get next replacement pointer
                while fast < len(letters) and letters[fast] ==  0:
                    fast += 1
                
                # return string if there is no more replacement pointer available
                if fast >= len(letters):
                    return string
                
                # add replacement letter
                string += chr(ord("z") - fast)

                # Subtract from letters since we used a replacement letter
                letters[fast] -= 1
                
            # add remainder is any
            string += char * remain
                
        return string