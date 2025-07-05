class Solution:
    def kthCharacter(self, k: int) -> str:
        string = 'a'
        while len(string) < k:
            newWord = ''
            for char in string:
                newWord += chr(ord(char)+1)

            string += newWord 
        return string[k-1]
        