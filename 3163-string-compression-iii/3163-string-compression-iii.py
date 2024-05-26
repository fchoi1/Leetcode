class Solution:
    def compressedString(self, word: str) -> str:
        string = ""
        prev = word[0]
        count = 1
        for i, char in enumerate(word[1:]):
             
            if char == prev:
                count += 1
                if count == 9:
                    string += str(count)+prev
                    count = 0
            else:
                if count != 0:
                    string += str(count)+prev
                count = 1
                
            prev = char
        if count != 0:
            string += str(count)+prev
        #"aaaaaaaaay"
        return string
        