import numpy as np
import json

def nearest_neighbor(matrix):
    n = len(matrix)
    unvisited = set(range(1, n))
    path = [0]
    current_city = 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: matrix[current_city][city])
        path.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city

    path.append(0)  # Returning to the starting city to complete the cycle
    return path

def calculate_total_distance(path, matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += matrix[path[i]][path[i + 1]]
    return total_distance

# Example usage for 20 vertices:
num_vertices = 20
# Assuming you have a 20x20 distance matrix, replace the following line with your actual matrix
distance_matrix = np.array([
    [0,2495,1135,2117,623,1560,1641,1963,2210,788,1581,1533,1793,1241,510,1765,1442,875,1858,1401,2323],
    [2495, 0, 3366, 2290, 3118, 1345, 854, 1176, 1291, 1707, 2160, 1606, 702, 1820, 1985, 1838, 1515, 3370, 1643, 2874, 1418],
    [1135, 3366, 0, 1076, 512, 2021, 2512, 2190, 2075, 1923, 1206, 1760, 2664, 1546, 1645, 1528, 1851, 376, 1723, 492, 1948],
    [2117, 2290, 1076, 0, 1494, 945, 1436, 1114, 999, 2905, 536, 684, 1588, 876, 2627, 452, 775, 1358, 647, 716, 872],
    [623, 3118, 512, 1494, 0, 1773, 2264, 1942, 1827, 1411, 958, 1512, 2416, 1298, 1133, 1280, 1603, 252, 1475, 778, 1700],
    [1560, 1345, 2021, 945, 1773, 0, 491, 403, 650, 2348, 815, 261, 787, 475, 2070, 493, 170, 2025, 298, 1529, 763],
    [1641, 854, 2512, 1436, 2264, 491, 0, 322, 569, 2429, 1306, 752, 868, 966, 2151, 984, 661, 2516, 789, 2020, 682],
    [1963, 1176, 2190, 1114, 1942, 403, 322, 0, 247, 2751, 984, 430, 1190, 722, 2473, 662, 521, 2194, 467, 1698, 360],
    [2210, 1291, 2075, 999, 1827, 650, 569, 247, 0, 2998, 869, 677, 1437, 969, 2720, 547, 768, 2079, 352, 1583, 127],
    [788, 1707, 1923, 2905, 1411, 2348, 2429, 2751, 2998, 0, 2369, 2321, 1561, 2029, 278, 2553, 2230, 1663, 2646, 2189, 3111],
    [1581, 2160, 1206, 536, 958, 815, 1306, 984, 869, 2369, 0, 554, 1458, 340, 2091, 322, 645, 1210, 517, 714, 742],
    [1533, 1606, 1760, 684, 1512, 261, 752, 430, 677, 2321, 554, 0, 904, 292, 2043, 232, 91, 1764, 325, 1268, 790],
    [1793, 702, 2664, 1588, 2416, 787, 868, 1190, 1437, 1561, 1458, 904, 0, 1118, 1283, 1136, 813, 2668, 1085, 2172, 1550],
    [1241, 1820, 1546, 876, 1298, 475, 966, 722, 969, 2029, 340, 292, 1118, 0, 1751, 524, 305, 1550, 617, 1054, 1082],
    [510, 1985, 1645, 2627, 1133, 2070, 2151, 2473, 2720, 278, 2091, 2043, 1283, 1751, 0, 2275, 1952, 1385, 2368, 1911, 2833],
    [1765, 1838, 1528, 452, 1280, 493, 984, 662, 547, 2553, 322, 232, 1136, 524, 2275, 0, 323, 1532, 195, 1036, 558],
    [1442, 1515, 1851, 775, 1603, 170, 661, 521, 768, 2230, 645, 91, 813, 305, 1952, 323, 0, 1855, 416, 1359, 881],
    [875, 3370, 376, 1358, 252, 2025, 2516, 2194, 2079, 1663, 1210, 1764, 2668, 1550, 1385, 1532, 1855, 0, 1727, 642, 1952],
    [1858, 1643, 1723, 647, 1475, 298, 789, 467, 352, 2646, 517, 325, 1085, 617, 2368, 195, 416, 1727, 0, 1231, 465],
    [1401, 2874, 492, 716, 778, 1529, 2020, 1698, 1583, 2189, 714, 1268, 2172, 1054, 1911, 1036, 1359, 642, 1231, 0, 1456],
    [2323, 1418, 1948, 872, 1700, 763, 682, 360, 127, 3111, 742, 790, 1550, 1082, 2833,558,881,1952,465,1456,0]])

tsp_path = nearest_neighbor(distance_matrix)
total_distance = calculate_total_distance(tsp_path, distance_matrix)

print("TSP Path:", tsp_path)
print("Total Distance:", total_distance)
#print(len(distance_matrix))

my_dict = {i: f'n{i-1}' for i in range(1, 21)}
my_dict[0] = 'r0'

# Printing the dictionary
#print(my_dict)
key_list = [my_dict[index] for index in tsp_path]

# Printing the result
#print(key_list)
data = {"v0": {"path": key_list}}

# Specify the file path where you want to save the JSON file
file_path = "level0_output.json"

# Write the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, separators=(',', ':'))
