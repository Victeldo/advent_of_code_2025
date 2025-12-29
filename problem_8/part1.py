### need to re-order junction boxes greedily based on shortest distance

### practice input has 20 values, need to make 10 pairs

### real has 1000 values, need to make 1000 pairs
import time

"""
pseudocode:
first make X pairs of the shortest distance
then form circuits based on pairs
then find 3 largest circuits (chain together pairs)
then merge circuits if they share a point.
then return product of 3 largest circuits
"""

MAX_PAIRS = 1000

def find_distance(point1, point2):
    return ((point1[0] - point2[0])**2  + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5

shortest_distances = [] ## (point1, point2, distance)

# first format the points
input = open('inputs/input.txt', 'r').read()
points = input.split('\n')
for idx, point in enumerate(points):
    point = point.split(',')
    point = (int(point[0]), int(point[1]), int(point[2]))
    points[idx] = point
    print("in iteration, idx:", idx)

# print(points)
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        print("in nested for loop, i:", i, "j:", j)
        distance = find_distance(points[i], points[j])
        # if not any((points[i], points[j]) == (a, b) or (points[i], points[j]) == (b, a) for a, b, _ in shortest_distances):
        #     shortest_distances.append((points[i], points[j], distance))
        shortest_distances.append((points[i], points[j], distance))

shortest_distances.sort(key=lambda x: x[2])

print("out of nested for loop")
# for distance in shortest_distances:
#     print(distance)

# print(shortest_distances[0])

circuits = [] ## list of lists, each list is a circuit

## append to circuit if point 1 or point 2 exists in the circuit. if not in any circuits, create a new circuit.

def point_in_circuit(circuit, point1, point2):
    if point1 in circuit:
        return 1
    if point2 in circuit:
        return 2
    else:
        return 0

for i in range(MAX_PAIRS):
    point1 = shortest_distances[i][0]
    point2 = shortest_distances[i][1]
    if len(circuits) == 0:
        circuits.append([point1, point2])
    else:
        not_in_circuit = True
        print("in else loop" + str(time.time()))
        for circuit in circuits:
            if point1 in circuit and point2 in circuit:
                not_in_circuit = False
                break
            if point1 in circuit and point2 not in circuit:
                circuit.append(point2)
                not_in_circuit = False
            elif point2 in circuit and point1 not in circuit:
                circuit.append(point1)
                not_in_circuit = False
        if not_in_circuit:
            circuits.append([point1, point2])
print("out of for loop")
## now need to merge circuits if they share a point.

for i in range(len(circuits) - 1):
    j = i + 1
    while j < len(circuits):
        print("in while loop" + str(i) + " " + str(j))
        circuit_set_i = set(circuits[i])
        circuit_set_j = set(circuits[j])
        if len(circuit_set_i & circuit_set_j) > 0:
            circuits[i] = list(circuit_set_i | circuit_set_j)
            circuits.pop(j)
            j = i + 1
        else:
            j += 1

circuits.sort(key=len, reverse=True)
total = 1
for i in range(3):
    total *= len(circuits[i])
print(total)