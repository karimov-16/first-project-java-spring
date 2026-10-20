import numpy as np

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

seed = int(ID[-3:])

print("ID:", ID)
print("seed (last three digits of ID):", seed)
print("Surname:", SURNAME)

print("ID backwards:", ID[::-1])
print("Surname backwards:", SURNAME[::-1])

np.random.seed(seed)
high = int(ID[-2:])
shape = (2 + int(ID[-2]), 2 + int(ID[-1]))
A = np.random.randint(0, high + 1, size=shape)

print("Size of array A:", A.size)
print("Shape of array A:", A.shape)
print("Sum of all numbers in array A:", A.sum())
print("Array A:")
print(A)
