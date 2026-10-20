import math
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

# 1. by hand
n = len(U)
mean = sum(U) / n
std_sample_hand = math.sqrt(sum((xi - mean) ** 2 for xi in U) / (n - 1))
std_pop_hand = math.sqrt(sum((xi - mean) ** 2 for xi in U) / n)
print("Sample std by hand:          ", std_sample_hand)
print("Population std by hand:      ", std_pop_hand)

# 2. statistics
print("Sample std statistics:       ", statistics.stdev(U))
print("Population std statistics:   ", statistics.pstdev(U))

# 3. numpy
print("Sample std np.std(ddof=1):   ", np.std(U, ddof=1))
print("Population std np.std:       ", np.std(U))

# 4. pandas
xs = pd.Series(U)
print("Sample std Series.std():     ", xs.std())
print("Population std std(ddof=0):  ", xs.std(ddof=0))
