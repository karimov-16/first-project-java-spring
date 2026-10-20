import numpy as np

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

sumID = 21
sumID_0 = 14
sumID_1 = 21
n = 2
k = 3
seed = 90
first3 = 750

print("Name:", NAME)
print("Surname:", SURNAME)
print("ID:", ID)

print("sumID   (sum of digits of ID):", sumID)
print("sumID_0 (sum of digits of ID without first digit from the left):", sumID_0)
print("sumID_1 (sum of digits of ID without first digit from the right):", sumID_1)
print("n =", n, ", k =", k)
print("seed (last three digits of ID):", seed)

np.random.seed(seed)
A = np.random.randint(0, sumID_0, size=(5 * sumID_0, 5 * sumID_1))
print("\nSum of A:", A.sum())
print("First row of A:", A[0])
print("Last row of A:", A[-1])

np.random.seed(seed)
B = np.random.randint(0, sumID_1, size=(5 * sumID_1, 5 * sumID_0))
print("\nSum of B:", B.sum())
print("First row of B:", B[0])
print("Last row of B:", B[-1])

a = A[n:n + k * k:k, k:k + n * n:n].copy()
print("\nShape of a:", a.shape)
print("Sum of a:", a.sum())
print("a:")
print(a)
a[-1, -1] = first3
print("a after replacing last element with", first3, ":")
print(a)

b = B[n:n + k * k:k, k:k + n * n:n]
print("\nShape of b:", b.shape)
print("Sum of b:", b.sum())
print("b:")
print(b)
b[-1, -1] = first3
print("b after replacing last element with", first3, ":")
print(b)

print("\na + b:")
print(a + b)
print("Sum of A (unchanged - a was a copy):", A.sum())
print("Sum of B (changed - b is a view):", B.sum())
