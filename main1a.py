import json
import numpy as np

json_data="""{
  "n_neighbourhoods": 20,
  "n_restaurants": 1,
  "neighbourhoods": {
    "n0": {
      "order_quantity": 70,
      "distances": [
        0,
        2953,
        1170,
        1677,
        1318,
        2055,
        591,
        3050,
        2626,
        1864,
        277,
        2499,
        769,
        1463,
        2006,
        2516,
        2394,
        997,
        1099,
        421
      ]
    },
    "n1": {
      "order_quantity": 70,
      "distances": [
        2953,
        0,
        1783,
        1276,
        1635,
        898,
        2458,
        97,
        423,
        1089,
        3026,
        664,
        2280,
        1600,
        1057,
        535,
        559,
        2182,
        2208,
        2532
      ]
    },
    "n2": {
      "order_quantity": 90,
      "distances": [
        1170,
        1783,
        0,
        507,
        148,
        885,
        675,
        1880,
        1456,
        694,
        1447,
        1697,
        497,
        2633,
        2090,
        1346,
        1224,
        2167,
        2269,
        953
      ]
    },
    "n3": {
      "order_quantity": 50,
      "distances": [
        1677,
        1276,
        507,
        0,
        359,
        752,
        1182,
        1373,
        1325,
        187,
        1750,
        1566,
        1004,
        2502,
        1959,
        839,
        717,
        2036,
        2138,
        1256
      ]
    },
    "n4": {
      "order_quantity": 70,
      "distances": [
        1318,
        1635,
        148,
        359,
        0,
        737,
        823,
        1732,
        1310,
        546,
        1391,
        1551,
        645,
        2487,
        1944,
        1198,
        1076,
        2021,
        2123,
        897
      ]
    },
    "n5": {
      "order_quantity": 90,
      "distances": [
        2055,
        898,
        885,
        752,
        737,
        0,
        1560,
        995,
        573,
        939,
        2128,
        814,
        1382,
        1750,
        1207,
        461,
        339,
        1284,
        1386,
        1634
      ]
    },
    "n6": {
      "order_quantity": 110,
      "distances": [
        591,
        2458,
        675,
        1182,
        823,
        1560,
        0,
        2555,
        2131,
        1369,
        868,
        2004,
        178,
        2054,
        1511,
        2021,
        1899,
        1588,
        1690,
        374
      ]
    },
    "n7": {
      "order_quantity": 70,
      "distances": [
        3050,
        97,
        1880,
        1373,
        1732,
        995,
        2555,
        0,
        424,
        1186,
        3123,
        665,
        2377,
        1601,
        1058,
        534,
        656,
        2279,
        2305,
        2629
      ]
    },
    "n8": {
      "order_quantity": 110,
      "distances": [
        2626,
        423,
        1456,
        1325,
        1310,
        573,
        2131,
        424,
        0,
        1512,
        2699,
        241,
        1953,
        1177,
        634,
        958,
        608,
        1855,
        1881,
        2205
      ]
    },
    "n9": {
      "order_quantity": 70,
      "distances": [
        1864,
        1089,
        694,
        187,
        546,
        939,
        1369,
        1186,
        1512,
        0,
        1937,
        1753,
        1191,
        2689,
        2146,
        652,
        904,
        2223,
        2325,
        1443
      ]
    },
    "n10": {
      "order_quantity": 70,
      "distances": [
        277,
        3026,
        1447,
        1750,
        1391,
        2128,
        868,
        3123,
        2699,
        1937,
        0,
        2572,
        1046,
        1536,
        2079,
        2589,
        2467,
        844,
        822,
        494
      ]
    },
    "n11": {
      "order_quantity": 110,
      "distances": [
        2499,
        664,
        1697,
        1566,
        1551,
        814,
        2004,
        665,
        241,
        1753,
        2572,
        0,
        1826,
        1036,
        493,
        1199,
        849,
        1728,
        1754,
        2078
      ]
    },
    "n12": {
      "order_quantity": 110,
      "distances": [
        769,
        2280,
        497,
        1004,
        645,
        1382,
        178,
        2377,
        1953,
        1191,
        1046,
        1826,
        0,
        2232,
        1689,
        1843,
        1721,
        1766,
        1868,
        552
      ]
    },
    "n13": {
      "order_quantity": 90,
      "distances": [
        1463,
        1600,
        2633,
        2502,
        2487,
        1750,
        2054,
        1601,
        1177,
        2689,
        1536,
        1036,
        2232,
        0,
        543,
        2135,
        1785,
        692,
        718,
        1680
      ]
    },
    "n14": {
      "order_quantity": 50,
      "distances": [
        2006,
        1057,
        2090,
        1959,
        1944,
        1207,
        1511,
        1058,
        634,
        2146,
        2079,
        493,
        1689,
        543,
        0,
        1592,
        1242,
        1235,
        1261,
        1585
      ]
    },
    "n15": {
      "order_quantity": 90,
      "distances": [
        2516,
        535,
        1346,
        839,
        1198,
        461,
        2021,
        534,
        958,
        652,
        2589,
        1199,
        1843,
        2135,
        1592,
        0,
        350,
        1745,
        1771,
        2095
      ]
    },
    "n16": {
      "order_quantity": 110,
      "distances": [
        2394,
        559,
        1224,
        717,
        1076,
        339,
        1899,
        656,
        608,
        904,
        2467,
        849,
        1721,
        1785,
        1242,
        350,
        0,
        1623,
        1649,
        1973
      ]
    },
    "n17": {
      "order_quantity": 90,
      "distances": [
        997,
        2182,
        2167,
        2036,
        2021,
        1284,
        1588,
        2279,
        1855,
        2223,
        844,
        1728,
        1766,
        692,
        1235,
        1745,
        1623,
        0,
        102,
        1214
      ]
    },
    "n18": {
      "order_quantity": 70,
      "distances": [
        1099,
        2208,
        2269,
        2138,
        2123,
        1386,
        1690,
        2305,
        1881,
        2325,
        822,
        1754,
        1868,
        718,
        1261,
        1771,
        1649,
        102,
        0,
        1316
      ]
    },
    "n19": {
      "order_quantity": 110,
      "distances": [
        421,
        2532,
        953,
        1256,
        897,
        1634,
        374,
        2629,
        2205,
        1443,
        494,
        2078,
        552,
        1680,
        1585,
        2095,
        1973,
        1214,
        1316,
        0
      ]
    }
  },
  "restaurants": {
    "r0": {
      "neighbourhood_distance": [
        797,
        2156,
        563,
        880,
        521,
        1258,
        302,
        2253,
        1829,
        1067,
        884,
        1702,
        162,
        2070,
        1527,
        1719,
        1597,
        1604,
        1706,
        390
      ],
      "restaurant_distance": [
        0
      ]
    }
  },
  "vehicles": {
    "v0": {
      "start_point": "r0",
      "speed": "INF",
      "capacity": 600
    }
  }
}"""
data = json.loads(json_data)

# Extract the distance matrix from the JSON data
neighbourhoods = data["neighbourhoods"]
n_neighbourhoods = data["n_neighbourhoods"]

distance_matrix = np.zeros((n_neighbourhoods, n_neighbourhoods))

for i in range(n_neighbourhoods):
    for j in range(n_neighbourhoods):
        distance_matrix[i][j] = neighbourhoods[f'n{i}']["distances"][j]

# Print the distance matrix
print("Distance Matrix:")
#print(distance_matrix)

#--------------------------------------------------------------------------------

import numpy as np

def calculate_total_distance(path, matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += matrix[path[i]][path[i + 1]]
    return total_distance


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

# Example usage:
num_vertices = 20
capacity = 600
quantity=[70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110]

resulting_routes = clarke_wright_savings(distance_matrix, quantity, capacity)

for i, route in enumerate(resulting_routes):
    print(f"Route {i + 1}: {route}")

total_distance = sum(calculate_total_distance(route, distance_matrix) for route in resulting_routes)
print("Total Distance:", total_distance)
