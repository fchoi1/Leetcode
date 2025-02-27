class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # b a b a d
        def checkPali(s, left, right):
          
          while left > 0 and right+1 < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            if s[left] != s[right]:
              left += 1
              right -= 1
              break

          return left, right+1
        
        start = 0
        end = 1
        for i in range(len(s)):
          if i+1 < len(s) and s[i] == s[i+1]:
            doubleL, doubleR = checkPali(s, i, i+1)
            if  doubleR - doubleL > end - start:
              start = doubleL
              end = doubleR
          
          singleL, singleR = checkPali(s, i, i)
          if singleR - singleL > end - start:
              start = singleL
              end = singleR
        
        return s[start:end]
          
          