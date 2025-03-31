class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        eq = {}
        for (a,b), val in zip(equations, values):
            if a not in eq:
                eq[a] = {}
            if b not in eq:
                eq[b] = {}
            eq[a][b] = val
            eq[b][a] = 1/val

        print(eq)

        def eval(a,target,val, seen):
            if a not in eq or a in seen:
                return -1
            seen.add(a)

            curr = eq[a]
            if target in curr:
                print("fond", val,  eq[a][target])
                return val * eq[a][target]
            
            for nextVal, n in curr.items():
                check = eval(nextVal, target, n * val, seen)
                if check != -1:
                    return check
            
            return -1
            
        
        ans = []
        for c,d in queries:
            ans.append(eval(c,d,1, set()))
            
        return ans