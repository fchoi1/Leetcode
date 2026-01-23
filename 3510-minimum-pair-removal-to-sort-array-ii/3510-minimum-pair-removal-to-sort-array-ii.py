class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
      
        N = len(nums)
        linked = { N - 1: (N - 2, None) } # idx:  (prevIdx, currIdx)

        # note because we store left index, update the double linked list is different for prev and next
        heap = [] # stores (sum, left index) -
        remove = set()

        # Pre-process data structures
        for i, (prev, curr) in enumerate(zip(nums, nums[1:])):

            # construct linked
            if i == 0:
                linked[i] = (None, i + 1)
            else:
                linked[i] = (i - 1, i + 1)
            
            # construct index to remove
            if curr < prev:
                remove.add(i)

            # construct heap
            heappush(heap, (prev + curr, i))

        ops = 0

        # We stop loop once we get rid of all index to remove
        while heap and len(remove) > 0:
      
            lowest, idx = heappop(heap)
            prevIdx, nextIdx = linked[idx]


            #### check if we should skip counting ops due to stale data

            # already removed since None
            if nums[idx] == None:
                continue

            # check is entry is valid up to date values, or skip if its the last element
            if (nextIdx != None and lowest != nums[idx] + nums[nextIdx]) or nextIdx == None:
                continue
       

            # Update indexes to remove
            remove.discard(idx)
            
            # increment ops 
            ops += 1

            # update new lowest value to idx in nums
            nums[idx] = lowest

            #### Double linked list updates - The main complex logic

            # Update/add prev idx to heap
            if prevIdx != None:
                
                # update prev link
                prevPrevIdx, prevNextIdx = linked[prevIdx]
                linked[prevIdx] = (prevPrevIdx, idx)

                # Check if this idx needs to be removed
                if nums[prevIdx] > lowest:
                    remove.add(prevIdx)
                # discard from remove since its valid now
                else:
                    remove.discard(prevIdx)

                heappush(heap, (nums[prevIdx] + lowest, prevIdx))
            
            # Update/add next idx to heap
            if nextIdx != None:
                # remove nextIdx from previous
                nums[nextIdx] = None
                remove.discard(nextIdx)

                # update curr link
                _, nextNextIdx = linked[nextIdx]
                linked[idx] = (prevIdx, nextNextIdx)

                # update future link
                if nextNextIdx != None:
                    linked[nextNextIdx] = (idx, linked[nextNextIdx][1])

                    # Check if idx needs to be removed
                    if lowest > nums[nextNextIdx]:
                        remove.add(idx)

                    heappush(heap, (lowest +  nums[nextNextIdx], idx))
        return ops 
            

            
      
            