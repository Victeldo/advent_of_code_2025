
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
This function finds the best circuit by iterating through the shortest distances and adding the points to the circuit until all points are in the circuit.
    Args:
        shortest_distances: The list of shortest distances
        points: The list of points
    Returns:
        The product of the last two points connected in the best circuit
    
    Note: This function is greedy and just keeps re-searching the whole shortest distances list until all points are in the circuit.
"""
def find_best_circuit(shortest_distances, points):
    circuit = [shortest_distances[0][0], shortest_distances[0][1]]
    while len(circuit) < len(points):
        for distance in shortest_distances:
            current_points = (distance[0], distance[1])
            if distance[0] in circuit and distance[1] not in circuit:
                circuit.append(distance[1])
                break
            elif distance[1] in circuit and distance[0] not in circuit:
                circuit.append(distance[0])
                break
            else:
                continue
        if len(circuit) == len(points):
            break
    return current_points[0][0] * current_points[1][0]


input = open('inputs/input.txt', 'r').read()
points = format_input(input)
shortest_distances = find_shortest_distances(points)

print(find_best_circuit(shortest_distances, points))