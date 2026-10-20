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
var_sample_hand = sum((xi - mean) ** 2 for xi in U) / (n - 1)
var_pop_hand = sum((xi - mean) ** 2 for xi in U) / n
print("Sample variance by hand:          ", var_sample_hand)
print("Population variance by hand:      ", var_pop_hand)

# 2. statistics
print("Sample variance statistics:       ", statistics.variance(U))
print("Population variance statistics:   ", statistics.pvariance(U))

# 3. numpy
print("Sample variance np.var(ddof=1):   ", np.var(U, ddof=1))
print("Population variance np.var:       ", np.var(U))

# 4. pandas
xs = pd.Series(U)
print("Sample variance Series.var():     ", xs.var())
print("Population variance var(ddof=0):  ", xs.var(ddof=0))
