class Solution:
    def hasMatch(self, s: str, p: str) -> bool:


        pre = p[:p.index('*')] 
        post = p[p.index('*')+1:]    
        
        if pre not in s:
            return False

        s_pre = s.index(pre)
        return post in s[s_pre + len(pre):]


        