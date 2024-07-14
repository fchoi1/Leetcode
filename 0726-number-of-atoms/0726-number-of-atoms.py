class Solution:
    def countOfAtoms(self, formula: str) -> str:

        # returns index and the number found
        def getNumber(i):
            count = ''
            while i < len(formula) and formula[i].isdigit():
                count += formula[i]
                i += 1
            return (i, 1) if not count else (i, int(count))

        atoms = defaultdict(int) # total atom counts
        currEl = defaultdict(int)
        el = None
        stack = []
        i = 0
        while i < len(formula):
            char = formula[i]

            # get total number count
            if char.isdigit():
                i, count = getNumber(i) # getNumber auto increments to next non-digit index
                currEl[el] += count
                el = None
            #if letter
            elif char.isalpha():

                # If uppercase update new element name and count
                if char == char.upper():
                    if el: 
                        currEl[el] += 1
                    el = char

                # If lowercase add to elemenet name
                elif char == char.lower():
                    el += char
                i += 1
            else:
                # If char is a bracket add Element name count
                if el:
                    currEl[el] += 1
                el = None

                if char == '(':
                    stack.append(currEl)
                    currEl = defaultdict(int)
                    i += 1 # increment i
                else:
                    i, count = getNumber(i+1) # getNumber auto increments to next non-digit index
        
                    for element, c in currEl.items():
                        if stack:
                            stack[-1][element] += c * count # update counts to next stack items
                        else:
                            atoms[element] += c * count

                    if stack:
                        currEl = stack.pop() # pop to get next level brackets

        # One last level check
        for element, c in currEl.items():
            atoms[element] += c 

        # Edge case to check last element 
        if formula[-1].isalpha():
            atoms[el] += 1            

        # For output and sorting elements
        elements = ''
        for key in  sorted(atoms.keys()):
            elements += f'{key}{atoms[key] if atoms[key] > 1 else ""}'  
        return elements