
"""
This function finds the euclidean distance between two points in 3D space.
    Args:
        point1: The first point
        point2: The second point
    Returns:
        The distance between the two points
"""
def find_distance(point1, point2):
    return ((point1[0] - point2[0])**2  + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5

"""
This function formats the input into a list of points.
    Args:
        input: The input string
    Returns:
        A list of points
"""
def format_input(input):
    input = input.split('\n')
    points = []
    for line in input:
        point = line.split(',')
        point = (int(point[0]), int(point[1]), int(point[2]))
        points.append(point)
    return points

"""
This function finds the shortest distances between all points.
    Args:
        points: The list of points
    Returns:
        A sorted list of shortest distances between all points
"""
def find_shortest_distances(points):
    shortest_distances = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            distance = find_distance(points[i], points[j])
            shortest_distances.append((points[i], points[j], distance))
    shortest_distances.sort(key=lambda x: x[2])
    return shortest_distances

"""
This function finds the circuits based on the shortest distances.
    Args:
        shortest_distances: The list of shortest distances
    Returns:
        A list of circuits, where each circuit is a list of points

    Note: This function does not merge circuits if they share a point.
"""
def find_circuits(shortest_distances):
    circuits = []
    for i in range(MAX_PAIRS):
        point1 = shortest_distances[i][0]
        point2 = shortest_distances[i][1]
        if len(circuits) == 0:
            circuits.append([point1, point2])
        else:
            not_in_circuit = True
            for circuit in circuits:
                if point1 in circuit and point2 in circuit:
                    not_in_circuit = False
                    break
                elif point1 in circuit and point2 not in circuit:
                    circuit.append(point2)
                    not_in_circuit = False
            if not_in_circuit:
                circuits.append([point1, point2])
    return circuits

"""
This function merges circuits if they share a point.
    Args:
        circuits: The list of circuits
    Returns:
        A list of circuits, where each circuit is a list of points
"""
def merge_circuits(circuits):
    for i in range(len(circuits) - 1):
        j = i + 1
        while j < len(circuits):
            circuit_set_i = set(circuits[i])
            circuit_set_j = set(circuits[j])
            if len(circuit_set_i & circuit_set_j) > 0:
                circuits[i] = list(circuit_set_i | circuit_set_j)
                circuits.pop(j)
                j = i + 1
            else:
                j += 1
    return circuits

MAX_PAIRS = 1000
input = open('inputs/input.txt', 'r').read()

points = format_input(input)

# find and sort shortest distances between all points
shortest_distances = find_shortest_distances(points)

# form circuits based on shortest distances with upper limit of MAX_PAIRS
raw_circuits = find_circuits(shortest_distances)

# merge circuits if they share a point
circuits = merge_circuits(raw_circuits)

circuits.sort(key=len, reverse=True)
total = 1
for i in range(3):
    total *= len(circuits[i])
print(total)


