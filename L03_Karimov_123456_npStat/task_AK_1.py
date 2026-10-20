import numpy as np

# ====== YOUR DATA (change only these lines) ======
NAME = "Abu"
SURNAME = "Karimov"
ID = "123456"            # your student ID
# ==================================================

# 1. variables
seed = int(ID[-3:])      # last three digits of the ID

# 2. print variables
print("ID:", ID)
print("seed (last three digits of ID):", seed)
print("Surname:", SURNAME)

# 3. print backwards
print("ID backwards:", ID[::-1])
print("Surname backwards:", SURNAME[::-1])

# 4. random array
np.random.seed(seed)
high = int(ID[-2:])                          # last two digits of ID
shape = (2 + int(ID[-2]), 2 + int(ID[-1]))   # (2 + penultimate digit, 2 + last digit)
A = np.random.randint(0, high + 1, size=shape)   # range [0, high] (inclusive)

print("Size of array A:", A.size)
print("Shape of array A:", A.shape)
print("Sum of all numbers in array A:", A.sum())
print("Array A:")
print(A)
