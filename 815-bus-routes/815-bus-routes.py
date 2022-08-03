import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routes_map = collections.defaultdict(set)
        # stop_id: {bus_id, bus_id}
        for stop_id, buses in enumerate(routes):
            for bus_id in buses:
                routes_map[bus_id].add(stop_id)

        queue = collections.deque([(source, 0)])

        took_stations = set()
        took_buses = set()

        while queue:
            stop, timer = queue.popleft()
            if stop == target:
                return timer
            for bus_index in routes_map[stop]:  # Loop buses in this stop
                if bus_index not in took_buses:
                    for station in routes[bus_index]:  # Loop stops in this bus
                        if station not in took_stations:
                            queue.append((station, timer + 1))
                            took_stations.add(station)
                    took_buses.add(bus_index)
        return -1