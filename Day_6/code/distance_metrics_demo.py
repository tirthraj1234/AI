from math import sqrt

# Points
A = (2, 3)
B = (5, 7)

# Euclidean Distance
euclidean = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

# Manhattan Distance
manhattan = abs(B[0] - A[0]) + abs(B[1] - A[1])

print("Euclidean Distance:", euclidean)
print("Manhattan Distance:", manhattan)