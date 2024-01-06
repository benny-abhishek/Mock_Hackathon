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
#print(distance_matrix)

# Distance matrix
# Capacity of the scooter carrier
capacity = 600

# Quantities required for each neighborhood
quantities = np.array([70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110])

# Initialize arrays to store the route for each customer and the savings for each pair of customers
routes = np.zeros(len(distance_matrix), dtype=int) + -1
savings = np.zeros((len(distance_matrix), len(distance_matrix)))

# Calculate the savings for each pair of customers
for i in range(len(distance_matrix)):
    for j in range(i+1, len(distance_matrix)):
        savings[i, j] = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]

# Sort the savings in descending order
sorted_savings_indices = np.argsort(savings[savings > 0])[::-1]

# Initialize an array to store the routes and the remaining capacity of each delivery
delivery_routes = []
delivery_capacities = [capacity] * len(distance_matrix)

# Initialize an array to store the slots and the remaining capacity of each slot
slot_routes = []
slot_capacities = [capacity] * len(distance_matrix)
#print(sorted_savings_indices)

# Iterate over the pairs of customers in descending order of savings
print(len(sorted_savings_indices))


for i in sorted_savings_indices:
    # If adding customer j to the route of customer i would not exceed the capacity of the vehicle
    if delivery_capacities[routes[i]] + quantities[j] <= capacity:
        # Add customer j to the route of customer i
        routes[j] = i
        delivery_capacities[routes[i]] += quantities[j]

        # If this is the first customer in a new route, add it to the list of delivery routes
        if routes[j] == -1:
            delivery_routes.append([j])
        # Otherwise, add it to the existing route
        else:
            delivery_routes[-1].append(j)

# Find the best slots for each delivery route
for delivery_route in delivery_routes:
    slot_route = []
    for i in delivery_route:
        if len(slot_routes) == 0 or slot_capacities[slot_routes[-1]] + quantities[i] > capacity:
            slot_routes.append([i])
            slot_capacities.append(capacity - quantities[i])
        else:
            slot_routes[-1].append(i)
            slot_capacities[-1] -= quantities[i]
        slot_route.append(slot_routes.index(delivery_route))
    print(f"Delivery {delivery_routes.index(delivery_route)+1}: {slot_route}")