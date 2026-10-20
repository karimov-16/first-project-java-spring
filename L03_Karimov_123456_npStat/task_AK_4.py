import statistics
import numpy as np
import pandas as pd

# ====== YOUR DATA (change only these lines) ======
NAME = "Abu"
SURNAME = "Karimov"
ID = "123456"            # your student ID
# ==================================================

seed = int(ID[-3:])                  # as in task 2
digit2 = int(ID[1])                  # second digit of ID
sumID = sum(int(d) for d in ID)      # sum of digits of ID

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))   # [digit2, sumID)
U = x.flatten().tolist()             # 1-D data (Python list) used for statistics

x1 = np.array(U)      # numpy array
x2 = pd.Series(U)     # pandas series

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
