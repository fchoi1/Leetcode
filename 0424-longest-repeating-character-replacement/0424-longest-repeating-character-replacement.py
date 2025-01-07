class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
#       subsetCount = [0] * 26
#       maxCount = 0
#       maxLength = 0
#       startIndex = 0
#       endIndex = 0
      
#       for i in range(len(s)):

#         while (endIndex - startIndex) - maxCount <= k:
#           subsetCount[ord(s[endIndex]) - ord('A')] += 1
#           maxCount = max(maxCount, subsetCount[ord(s[endIndex]) - ord('A')])
#           maxLength = max(maxLength, endIndex - startIndex)
#           endIndex += 1

#           if endIndex >= len(s) and (endIndex - startIndex) - maxCount <= k:
#             maxLength = max(maxLength, endIndex - startIndex)
#             return maxLength
#           elif endIndex >= len(s):
#             return maxLength
          
#         subsetCount[ord(s[startIndex]) - ord('A')] -= 1
#         maxCount = max(subsetCount)
#         startIndex += 1

#       return maxLength
    
      subsetCount = [0] * 26
      maxCount = 0
      maxLength = 0
      startIndex = 0
      endIndex = 0

      while endIndex < len(s):
        
        if (endIndex - startIndex) - maxCount <= k:
          
          subsetCount[ord(s[endIndex]) - ord('A')] += 1
          maxCount = max(maxCount, subsetCount[ord(s[endIndex]) - ord('A')])
          maxLength = max(maxLength, endIndex - startIndex)
          endIndex += 1

        else:
          subsetCount[ord(s[startIndex]) - ord('A')] -= 1
          maxCount = max(subsetCount)
          startIndex += 1
          
      if (endIndex - startIndex) - maxCount <= k:
        maxLength = max(maxLength, endIndex - startIndex)
      return maxLength 
        
      
      
      
        