class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:


        stops_dict = defaultdict(list)
        for i, bus in enumerate(routes):
            for stop in bus:
                stops_dict[stop].append(i)

        q = [source]
        # no need to take same bus and stop again
        seen_stops = set() 
        seen_bus = set()

        buses = 0

        while q:
            temp = []

            for curr in q:
                if curr == target:
                    return buses
                
                # Optimize
                if curr in seen_stops:
                    continue

                seen_stops.add(curr)


                # get list of bus to get to dest
                for bus in stops_dict[curr]:
                    if bus in seen_bus:
                        continue
                    seen_bus.add(bus)

                    for r in routes[bus]:
                        if r in seen_stops:
                            continue
                        temp.append(r)

            buses += 1
            q = temp

        return -1