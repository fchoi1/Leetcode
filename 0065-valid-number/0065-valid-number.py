class Solution:
    def isNumber(self, s: str) -> bool:
        if s.lower().find('inf') != -1 or s.lower().find('nan') != -1:
            return False

        def isNum(string):
            try:
                float(string)
            except ValueError:
                return False
            return True
        eIndex = s.find('e')
        EIndex = s.find('E')
        index = eIndex if eIndex != -1 else EIndex

        if index != -1:
            string = s[:index]
            try:
                int(s[index+1:])
            except ValueError:
                return False
            return isNum(string)
        else:
            return isNum(s)
        
        
