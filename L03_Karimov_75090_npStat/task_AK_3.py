import statistics
import numpy as np

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

seed = int(ID[-3:])
digit2 = int(ID[1])
sumID = sum(int(d) for d in ID)

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))
U = x.flatten().tolist()

print("Name:", NAME)
print("Surname:", SURNAME)
print("ID:", ID)
print("seed (last three digits of ID):", seed)
print("Second digit of ID:", digit2)
print("Sum of digits of ID:", sumID)

print("\nType of x:", type(x))
print("x:")
print(x)

mean_1 = sum(U) / len(U)
mean_2 = statistics.mean(U)
mean_3 = statistics.fmean(U)
print("\nMean sum(U)/len(U):   ", mean_1)
print("Mean statistics.mean: ", mean_2)
print("Mean statistics.fmean:", mean_3)
