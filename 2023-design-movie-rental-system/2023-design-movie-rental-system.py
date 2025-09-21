class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        
        self.rented = [] # heap (price, shop, movie)
        self.unrented = defaultdict(list) # movie: heap (price, shop)
        self.prices = defaultdict(int) # (shop, movie): (price, isRented)

        for shop, movie, price in entries:
            heappush(self.unrented[movie], (price, shop))
            self.prices[(shop, movie)] = (price, False)

    def search(self, movie: int) -> List[int]:
        heap = self.unrented[movie]
        count = 0
        cheapest = []
        prev = None
        while heap and count < 5:
            curr = heappop(heap)
            _, shop = curr

            # check dupes or if rented and ignore
            if prev == curr or ((shop, movie) in self.prices and self.prices[(shop,movie)][1]):
                continue
            cheapest.append(curr)
            count += 1
            prev = curr
        
        for curr in cheapest:
            heappush(heap, curr)
        
        return [curr[1] for curr in cheapest]
        

    def rent(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        if key not in self.prices:
            print("ERROR Rent")

        p, _ = self.prices[key]
        self.prices[key] = (p, True)
        heappush(self.rented, (p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        if key not in self.prices:
            print("ERROR Drop")

        p, _ = self.prices[key]
        self.prices[key] = (p, False)
        heappush(self.unrented[movie], (p, shop))
        
    def report(self) -> List[List[int]]:
        count = 0
        cheapest = []
        prev = None

        while self.rented and count < 5:
            curr = heappop(self.rented)
            _, shop, movie = curr
            if prev == curr or ((shop, movie) in self.prices and not self.prices[(shop,movie)][1]):
                continue
            cheapest.append(curr)
            count += 1
            prev = curr
        
        for curr in cheapest:
            heappush(self.rented, curr)
        
        return [(curr[1], curr[2]) for curr in cheapest]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()