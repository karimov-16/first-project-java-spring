import statistics
import numpy as np
from scipy import stats

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

# 1. statistics
print("Mode statistics.mode:          ", statistics.mode(U))
print("Multimode statistics.multimode:", statistics.multimode(U))

# 2. scipy
m = stats.mode(U)
print("Mode scipy.stats.mode:         ", m.mode, "(count:", m.count, ")")
values, counts = np.unique(U, return_counts=True)
print("Multimode (scipy/numpy):       ", values[counts == counts.max()])
