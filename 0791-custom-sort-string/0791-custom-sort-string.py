class Solution:
    def customSortString(self, order: str, s: str) -> str:        
        count = Counter(s)
        string = ""
        for char in order:
            if count[char]:
                string += char * count[char]
                del count[char]
        for char, freq in count.items():
            string += char * freq
        return string
        