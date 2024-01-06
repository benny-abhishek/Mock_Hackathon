import numpy as np
import json

with open("Input data\\level1a.json") as f:
   data = json.load(f)

# Extract the distance matrix from the JSON data
neighbourhoods = data["neighbourhoods"]
n_neighbourhoods = data["n_neighbourhoods"]

distance_matrix = np.zeros((n_neighbourhoods, n_neighbourhoods))

for i in range(n_neighbourhoods):
    for j in range(n_neighbourhoods):
        distance_matrix[i][j] = neighbourhoods[f'n{i}']["distances"][j]


distance_matrix = distance_matrix.astype(int)


def clarke_wright_savings(distance_matrix, quantity, capacity):
    n = len(distance_matrix)
    demand = [0] + quantity + [0]  # Adding the depot (vertex 0) with zero demand

    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            savings.append(((0, i, 0), (0, j, 0), distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]))

    savings.sort(key=lambda x: x[2], reverse=True)

    routes = [[0] for _ in range(n)]
    remaining_capacity = [capacity] * n

    for s in savings:
        (r1_start, r1_end, _), (r2_start, r2_end, _), saving = s

        if remaining_capacity[r1_end] >= demand[r2_end] and remaining_capacity[r2_end] >= demand[r1_end]:
            route1 = routes[r1_start] + routes[r1_end][1:]
            route2 = routes[r2_start] + routes[r2_end][1:]
            
            if route1[-1] == route2[0]:
                new_route = route1 + route2[1:]
                if sum(demand[vertex] for vertex in new_route) <= capacity:
                    routes[r1_start] = new_route
                    routes[r1_end] = []
                    remaining_capacity[r1_end] = 0
                    remaining_capacity[r2_end] -= demand[r1_end]

    routes = [route for route in routes if route]

    return routes

def calculate_total_distance(path, matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += matrix[path[i]][path[i + 1]]
    return total_distance

# Example usage:
num_vertices = 20
capacity = 600
quantity = np.random.randint(10, 50, size=num_vertices)
distance_matrix = np.random.randint(10, 100, size=(num_vertices, num_vertices))

resulting_routes = clarke_wright_savings(distance_matrix, quantity, capacity)

for i, route in enumerate(resulting_routes):
    print(f"Route {i + 1}: {route}")

total_distance = sum(calculate_total_distance(route, distance_matrix) for route in resulting_routes)
print("Total Distance:", total_distance)

