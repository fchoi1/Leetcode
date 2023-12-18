class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      if not nums:
        return 0
      
      tracker = {}
      maxLength = 1
      
      for n in nums:
        
        if n not in tracker:

          if  n+1 in tracker and n-1 in tracker:
            
            length =  1 + tracker[n+1]['length'] + tracker[n-1]['length']

            tracker[n] = { 'start': tracker[n-1]['start'], 'end': tracker[n+1]['end'], 'length':length }
            
            tracker[tracker[n+1]['end']]['length'] = length
            tracker[tracker[n+1]['end']]['start'] = tracker[tracker[n-1]['start']]['start']
            
            
            tracker[tracker[n-1]['start']]['length'] = length
            tracker[tracker[n-1]['start']]['end'] = tracker[tracker[n+1]['end']]['end']


            maxLength = max(maxLength, length)
            
            continue
            
          if n+1 in tracker:
            tracker[n] = { 'start': n, 'end': tracker[n+1]['end'], 'length': 1 + tracker[n+1]['length'] }
            
            tracker[tracker[n+1]['end']]['start'] = n
            tracker[tracker[n+1]['end']]['length'] += 1
            
            maxLength = max(maxLength, tracker[n]['length'])
            continue
            
          if n-1 in tracker:
             
            tracker[n] = { 'start': tracker[n-1]['start'], 'end': n, 'length': 1 + tracker[n-1]['length'] }
            
            tracker[tracker[n-1]['start']]['end'] = n
            tracker[tracker[n-1]['start']]['length'] += 1
            maxLength = max(maxLength, tracker[n]['length'])
            
            continue
            
          tracker[n] = { 'start': n, 'end': n, 'length': 1  }
         
          
      return maxLength