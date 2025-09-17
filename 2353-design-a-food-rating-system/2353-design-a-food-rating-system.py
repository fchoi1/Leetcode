class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # foods can lose rating
        # track each cuinse rating
        # get highest rating per cusine
        # binary search / heap

        self.heaps = defaultdict(list) # cusine: max heap (rating, food)
        self.ratings = {} # food: rating, cusine

        for i in range(len(foods)):
            f = foods[i]
            c = cuisines[i]
            r = ratings[i]

            heappush(self.heaps[c], (-r, f))
            self.ratings[f] = (-r, c)       

    def changeRating(self, food: str, newRating: int) -> None:
        # assum exist
        _, c = self.ratings[food]
        self.ratings[food] = (-newRating, c)
        heappush(self.heaps[c], (-newRating, food))  

    def highestRated(self, cuisine: str) -> str:
        r = self.heaps[cuisine]

        while self.heaps[cuisine] and self.ratings[self.heaps[cuisine][0][1]][0]!= self.heaps[cuisine][0][0]:
            heappop(self.heaps[cuisine])
        
        return self.heaps[cuisine][0][1] # return top

    

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


# heap[0] # highest rating
# but we need to check if this highest rating is valid 
# check against the rating dict if the rate == heap rating then it is a valid