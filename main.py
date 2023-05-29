import asyncio
import itertools

async def calculate_cost(route, distances):
    cost = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        cost += distances[city1][city2]
    # Add cost to return from the last city to city 1
    cost += distances[route[-1]][route[0]]
    return cost

async def main():
    n = int(input("Enter the number of cities: "))

    # Generate all permutations of cities except city 1
    cities = list(range(1, n + 1))
    permutations = list(itertools.permutations(cities))

    # Get distances between all permutations of cities
    distances = {}
    for i in range(1, n + 1):
        distances[i] = {}
        for j in range(1, n + 1):
            distances[i][j] = int(input(f"Enter the distance between city {i} and city {j}: "))

    shortest_route = None
    shortest_cost = float('inf')

    for route in permutations:
        # Add city 1 at the beginning and end of the route
        complete_route = route + (route[0],)
        cost = await calculate_cost(complete_route, distances)
        if cost < shortest_cost:
            shortest_cost = cost
            shortest_route = complete_route

    print("Shortest route:", shortest_route)
    print("Shortest cost:", shortest_cost)

asyncio.run(main())

