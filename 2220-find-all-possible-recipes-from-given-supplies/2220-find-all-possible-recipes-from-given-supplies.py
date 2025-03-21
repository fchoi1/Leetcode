class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    
        created = set(supplies)
        ingredients_dict = {r:i for r,i in zip(recipes, ingredients)}
        seen = set()
        
        def checkRecipe(r):
            if r in created:
                return True

            if r not in ingredients_dict or r in seen:
                return False

            seen.add(r) # edge case loop

            for i in ingredients_dict[r]:
                if not checkRecipe(i):
                    return False
            created.add(r)
            return True

        ans = []
        for r in recipes:
            if checkRecipe(r):
                ans.append(r)
        return ans
