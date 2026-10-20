import numpy as np

# ====== YOUR DATA (change only these lines) ======
NAME = "Abu"
SURNAME = "Karimov"
ID = "123456"            # your student ID
# ==================================================

# constants
sumID = sum(int(d) for d in ID)          # sum of digits of ID
sumID_0 = sum(int(d) for d in ID[1:])    # without first digit from the left
sumID_1 = sum(int(d) for d in ID[:-1])   # without first digit from the right
n = 2
k = 3
seed = int(ID[-3:])                      # int() drops a leading zero
first3 = int(ID[:3])                     # first three digits of ID

# 1. personal data
print("Name:", NAME)
print("Surname:", SURNAME)
print("ID:", ID)

# 2. constants
print("sumID   (sum of digits of ID):", sumID)
print("sumID_0 (sum of digits of ID without first digit from the left):", sumID_0)
print("sumID_1 (sum of digits of ID without first digit from the right):", sumID_1)
print("n =", n, ", k =", k)
print("seed (last three digits of ID):", seed)

# 3-7. array A
np.random.seed(seed)
A = np.random.randint(0, sumID_0, size=(5 * sumID_0, 5 * sumID_1))
print("\nSum of A:", A.sum())
print("First row of A:", A[0])
print("Last row of A:", A[-1])

# 8-12. array B
np.random.seed(seed)
B = np.random.randint(0, sumID_1, size=(5 * sumID_1, 5 * sumID_0))
print("\nSum of B:", B.sum())
print("First row of B:", B[0])
print("Last row of B:", B[-1])

# 13-17. a = COPY of slice of A, start [n,k], every k-th row, every n-th column, shape (k,n)
a = A[n:n + k * k:k, k:k + n * n:n].copy()
print("\nShape of a:", a.shape)
print("Sum of a:", a.sum())
print("a:")
print(a)
a[-1, -1] = first3                       # last element of a
print("a after replacing last element with", first3, ":")
print(a)

# 18-22. b = VIEW of slice of B, start [n,k], every k-th row, every n-th column, shape (k,n)
b = B[n:n + k * k:k, k:k + n * n:n]
print("\nShape of b:", b.shape)
print("Sum of b:", b.sum())
print("b:")
print(b)
b[-1, -1] = first3                       # changes B as well (b is a view)
print("b after replacing last element with", first3, ":")
print(b)

# 23-25
print("\na + b:")
print(a + b)
print("Sum of A (unchanged - a was a copy):", A.sum())
print("Sum of B (changed - b is a view):", B.sum())
