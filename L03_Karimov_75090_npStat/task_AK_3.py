import statistics
import numpy as np

# ====== YOUR DATA (change only these lines) ======
NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"             # your student ID
# ==================================================

seed = int(ID[-3:])                  # as in task 2
digit2 = int(ID[1])                  # second digit of ID
sumID = sum(int(d) for d in ID)      # sum of digits of ID

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))   # [digit2, sumID)
U = x.flatten().tolist()             # 1-D data (Python list) used for statistics

print("Name:", NAME)
print("Surname:", SURNAME)
print("ID:", ID)
print("seed (last three digits of ID):", seed)
print("Second digit of ID:", digit2)
print("Sum of digits of ID:", sumID)

print("\nType of x:", type(x))
print("x:")
print(x)

# Measures of location - mean
mean_1 = sum(U) / len(U)
mean_2 = statistics.mean(U)
mean_3 = statistics.fmean(U)
print("\nMean sum(U)/len(U):   ", mean_1)
print("Mean statistics.mean: ", mean_2)
print("Mean statistics.fmean:", mean_3)
