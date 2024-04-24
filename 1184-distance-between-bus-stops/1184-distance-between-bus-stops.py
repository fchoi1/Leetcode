class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        route = sum(distance[min(start,destination):max(start,destination)])
        return  min(total - route, route)
        