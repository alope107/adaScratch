'''
We are interested in finding the fewest number of buses needed to get from one bus station to another.

We are given a dictionary where the keys are the names of stations, and the values are a list of all the numbers of the bus routes that stop at that station. For example:

stations = {
    "Central Station": [3, 22, 99],
    "Ocean Point": [18],
    "Arts District": [3, 22, 6],
    "Fairground": [18],
    "Sandpiper Elementary School": [99, 6],
    "Bobcat Middle School": [3, 7, 6],
    "Falcon High School": [7, 18]
}

We can see that buses 3, 22, and 99 stop at Central Station.

We are also given the same information in reverse: a dictionary where they keys are the bus route numbers and the values are lists of stations that the route visits:

routes = {
    3: ['Central Station', 'Arts District', 'Bobcat Middle School'],
    22: ['Central Station', 'Arts District'],
    99: ['Central Station', 'Sandpiper Elementary School'],
    18: ['Ocean Point', 'Fairground', 'Falcon High School'],
    6: ['Arts District', 'Sandpiper Elementary School', 'Bobcat Middle School'],
    7: ['Bobcat Middle School', 'Falcon High School']
}

Note that this is the same information structured in a different way. The two dictionaries are guaranteed to be consistent with one another.

We can see that to get from Ocean Point to the Arts District one possible route would be as follows:

Ocean Point -> Falcon High School (Bus 18)
Falcon High School -> Bobcat Middle School (Bus 7)
Bobcat Middle School -> Arts District (Bus 6)

This route uses three buses. There is no route between Ocean Point that uses fewer buses.

Write a function that accepts a stations dictionary, a routes dictionary, and a start and end position. It should return the minimum number of buses needed to get from the start to the end.
'''

stations = {
    "Central Station": [3, 22, 99],
    "Ocean Point": [18],
    "Arts District": [3, 22, 6],
    "Fairground": [18],
    "Sandpiper Elementary School": [99, 6],
    "Bobcat Middle School": [3, 7, 6],
    "Falcon High School": [7, 18]
}

# MAKE SURE TO UPDATE ME IF CHANGING STATIONS
routes = {
    3: ['Central Station', 'Arts District', 'Bobcat Middle School'],
    22: ['Central Station', 'Arts District'],
    99: ['Central Station', 'Sandpiper Elementary School'],
    18: ['Ocean Point', 'Fairground', 'Falcon High School'],
    6: ['Arts District', 'Sandpiper Elementary School', 'Bobcat Middle School'],
    7: ['Bobcat Middle School', 'Falcon High School']
}

# UTILITY FOR UPDATING ROUTES, DELETE ME
# def station_to_route(stations):
#     routes_map = {}
#     for station, routes in stations.items():
#         for route in routes:
#             if route not in routes_map:
#                 routes_map[route] = []
#             routes_map[route].append(station)
#     return routes_map

def bus_count(stations, routes, start, end):
    # Initialize BFS queue
    # Will hold tuples
        # Element 0 of tuple is the location
        # Element 1 is how far away it is from the initial start
    # Begin with start location (which is 0 away from start)
    queue = [(start, 0)]
    # Start location is already visited
    visited = {start}
    while queue:
        # Dequeue and unpack
        current, length = queue.pop(0)
        # If we found the end
        if current == end:
            # Return the length from the start
            return length
        # For each of the possible bus routes to take
        for route in stations[current]:
            # For each of the stations that bus visits
            for station in routes[route]:
                # If we haven't already checked that station
                if station not in visited:
                    # Add it to visited and the back of the queue, incrementing length by one
                    visited.add(station)
                    queue.append((station, length+1))

assert bus_count(stations, routes, "Ocean Point", "Arts District") == 3
assert bus_count(stations, routes, "Falcon High School", "Fairground") == 1
assert bus_count(stations, routes, "Falcon High School", "Sandpiper Elementary School") == 2

print("All tests passed! Discuss time & space complexity if time remains.")
    