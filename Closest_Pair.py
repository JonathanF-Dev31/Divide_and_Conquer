import math

# Agregamos los índices al conjunto de puntos
P = [
    (120, 5), (95, 3), (130, 7), (200, 12), (110, 4),
    (160, 10), (125, 6), (90, 2), (135, 7), (80, 1),
    (100, 3), (180, 11), (175, 10), (140, 6), (115, 4),
    (85, 2), (190, 12), (105, 5), (150, 8), (165, 9),
    (155, 8), (145, 6), (170, 10), (88, 2), (112, 5),
    (138, 9), (148, 7), (132, 7), (108, 4), (118, 5)
]

# Agregamos el índice a cada punto para rastrear su posición original
P_indexed = [(p[0], p[1], i) for i, p in enumerate(P)]

def mergesort(Array, Coordinate):
    if len(Array) == 1:
        return Array
    mid_point = len(Array) // 2
    left_sorted = mergesort(Array[:mid_point], Coordinate)
    right_sorted = mergesort(Array[mid_point:], Coordinate)
    return merge(left_sorted, right_sorted, Coordinate)

def merge(A, B, Coordinate):
    i = j = 0
    C = []
    Coordinate = 0 if Coordinate == 'x' else 1
    while i < len(A) and j < len(B):
        if A[i][Coordinate] <= B[j][Coordinate]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:])
    C.extend(B[j:])
    return C

def Initial_Sort(P):
    Px = mergesort(P, 'x')
    Py = mergesort(P, 'y')
    return Px, Py

def Euclidean_Distance(P1, P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

def BruteForceClosestPair(Array):
    min_distance = float('inf')
    Target_Pair = (Array[0], Array[1])
    for i in range(len(Array)):
        for j in range(i + 1, len(Array)):
            d = Euclidean_Distance(Array[i], Array[j])
            if d < min_distance:
                min_distance = d
                Target_Pair = (Array[i], Array[j])
    return min_distance, Target_Pair[0], Target_Pair[1]

def Closest_Pair(Px, Py):
    if len(Px) <= 3:
        return BruteForceClosestPair(Px)

    mid = len(Px) // 2
    Qx = Px[:mid]
    Rx = Px[mid:]
    median_x = Px[mid][0]

    Qy = [p for p in Py if p[0] <= median_x]
    Ry = [p for p in Py if p[0] > median_x]

    d1, p1a, p1b = Closest_Pair(Qx, Qy)
    d2, p2a, p2b = Closest_Pair(Rx, Ry)

    if d1 < d2:
        min_distance = d1
        best_pair = (p1a, p1b)
    else:
        min_distance = d2
        best_pair = (p2a, p2b)

    Sy = [p for p in Py if abs(p[0] - median_x) < min_distance]

    for i in range(len(Sy)):
        for j in range(i+1, min(i + 7, len(Sy))):
            d = Euclidean_Distance(Sy[i], Sy[j])
            if d < min_distance:
                min_distance = d
                best_pair = (Sy[i], Sy[j])

    return min_distance, best_pair[0], best_pair[1]

# Ejecutar
Px, Py = Initial_Sort(P_indexed)
distance, p1, p2 = Closest_Pair(Px, Py)

# Imprimir resultado
print(f"Las dos personas mas cercanas son:")
print(f"Persona {p1[2]+1}: Capital = {p1[0]}, Experiencia = {p1[1]}")
print(f"Persona {p2[2]+1}: Capital = {p2[0]}, Experiencia = {p2[1]}")
print(f"Distancia euclidiana entre ellos: {distance:.4f}")
