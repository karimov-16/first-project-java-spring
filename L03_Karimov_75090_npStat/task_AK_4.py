import statistics
import numpy as np
import pandas as pd

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

seed = int(ID[-3:])
digit2 = int(ID[1])
sumID = sum(int(d) for d in ID)

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))
U = x.flatten().tolist()

x1 = np.array(U)
x2 = pd.Series(U)

print("Type x1:", type(x1))
print("Type x2:", type(x2))

print("\nMean of x1 (numpy):")
print("  sum/len:          ", sum(x1) / len(x1))
print("  statistics.fmean: ", statistics.fmean(x1))
print("  np.mean:          ", np.mean(x1))
print("  x1.mean():        ", x1.mean())

print("\nMean of x2 (pandas):")
print("  sum/len:          ", sum(x2) / len(x2))
print("  statistics.fmean: ", statistics.fmean(x2))
print("  x2.mean():        ", x2.mean())
